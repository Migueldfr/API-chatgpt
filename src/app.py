import openai
import os
from flask import Flask, render_template, request
import sqlite3
from datetime import datetime
import pymysql

# Creamos la ruta de nuestros archivos externos 
api_key_path = os.path.join(os.path.dirname(__file__), "api_key.txt")
# bbdd_path = os.path.join(os.path.dirname(__file__), "data/questions.db")

# Llamamos a la web server para desplegarla
app = Flask(__name__)
app.config['DEBUG'] = True

# Elaboramos un template de HTML con CSS y a su vez un video de fondo
@app.route("/")
def hello():
    return render_template('index.html')

# Creamos la funcion para la llamada a la API de CHATGPT
@app.route('/', methods=['POST'])
def my_form_post():
    api_key = request.form['api_key']
    openai.api_key = api_key
    #openai.api_key = open(api_key_path, "r").read()
    variable = request.form['variable']
    response = openai.Completion.create(engine = "text-davinci-003",
                                    prompt = variable + "Respuesta corta, por favor",
                                    max_tokens=500, temperature=0.9)
    
    # Cambiamos los valores sin codificar por sus correciones
    text_output = response.choices[0].text
    text_output = text_output.replace('\n', ' ')
    text_output = text_output.replace('\t', '    ')
    text_output = text_output.replace('\u00e1', 'á')
    text_output = text_output.replace('\u00e9', 'é')
    text_output = text_output.replace('\u00ed', 'í')
    text_output = text_output.replace('\u00f3', 'ó')
    text_output = text_output.replace('\u00fa', 'ú')
    
    # Añadimos a la base de datos en formato fecha y hora
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pregunta_respuesta = (now, variable, text_output)
    print('Pregunta respuesta:', pregunta_respuesta)
    # Conectamos con AWS 
    username = "admin"
    password = "12345678"
    host = "database-1.c10by1rrbsdg.us-east-2.rds.amazonaws.com" 
    port = 3306
    db = pymysql.connect(host = host,
                     user = username,
                     password = password,
                     cursorclass = pymysql.cursors.DictCursor)
    
    # Accedemos a la base de datos seleccionada
    crsr = db.cursor()
    crsr.connection.commit()
    use_db = '''USE PreguntasGPT'''
    crsr.execute(use_db)

    # Dentro de la base de datos, insertamos en la tabla elegida los datos obtenidos
    insert_data = '''INSERT INTO GPT (FECHA, PREGUNTAS, RESPUESTAS) VALUES ('%s', '%s', '%s')''' % pregunta_respuesta
    crsr.execute(insert_data)
    
    # Llevamos a cabo los cambios y cerramos la conexión con la base de datos
    db.commit()
    db.close()
    return render_template('index_2.html', text_output=text_output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)

