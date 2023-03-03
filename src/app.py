import openai
import os
from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

# Creamos la ruta de nuestros archivos externos 
api_key_path = os.path.join(os.path.dirname(__file__), "api_key.txt")
bbdd_path = os.path.join(os.path.dirname(__file__), "data/questions.db")
print(api_key_path)

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
    openai.api_key = open(api_key_path, "r").read()
    variable = request.form['variable']
    response = openai.Completion.create(engine = "text-davinci-003",
                                    prompt = variable + "Respuesta corta, por favor",
                                    max_tokens=500, temperature=0.9)
    
    # Cambiamos los valores sin codificar por sus correciones
    text_output = response.choices[0].text
    text_output = text_output.replace('\u00e1', 'á')
    text_output = text_output.replace('\u00e9', 'é')
    text_output = text_output.replace('\u00ed', 'í')
    text_output = text_output.replace('\u00f3', 'ó')
    text_output = text_output.replace('\u00fa', 'ú')

    # Añadimos a la base de datos en formato fecha y hora
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pregunta_respuesta = (now, variable, text_output)

    # Conectamos con la BBDD y a su vez lo insetarmos en ella 
    connection = sqlite3.connect(bbdd_path)
    crsr = connection.cursor()
    crsr.execute("INSERT INTO FAQ VALUES (?,?,?)", pregunta_respuesta)
    connection.commit()
    connection.close()
    return text_output + '<p><a href="/">Back</a></p>\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)

