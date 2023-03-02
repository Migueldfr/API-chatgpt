import openai
import os
from flask import Flask, render_template, request
import sqlite3
import datetime as dt
from datetime import datetime

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    openai.api_key = open("api_key.txt", "r").read()
    variable = request.form['variable']
    response = openai.Completion.create(engine = "text-davinci-003",
                                    prompt = variable + "Respuesta corta, por favor",
                                    max_tokens=500, temperature=0.9)
  
    text_output = response.choices[0].text
    text_output = text_output.replace('\n')
    text_output = text_output.replace('\t', '    ')
    text_output = text_output.replace('\u00e1', 'á')
    text_output = text_output.replace('\u00e9', 'é')
    text_output = text_output.replace('\u00ed', 'í')
    text_output = text_output.replace('\u00f3', 'ó')
    text_output = text_output.replace('\u00fa', 'ú')

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pregunta_respuesta = (now, variable, text_output)

    connection = sqlite3.connect("questions.db")
    crsr = connection.cursor()
    crsr.execute("INSERT INTO FAQ VALUES (?,?,?)", pregunta_respuesta)
    connection.commit()
    connection.close()
    return text_output + '<p><a href="/">Back</a></p>\n'

if __name__ == "__main__":
    app.run()

