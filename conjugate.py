from flask import Flask, render_template, request
from mlconjug3 import Conjugator
from mlconjug3 import ConjugManager 
# import os
import json

# conjugator = Conjugator(language='pt')
# verb = conjugator.conjugate('falar')
# print(verb["Indicativo"]["Indicativo Futuro do Presente Simples"])
# verb_indicativo =   {



app = Flask(__name__)




# https://mlconjug3.readthedocs.io/en/latest/readme.html



@app.route("/")
def index():
    return render_template('index.html')

@app.route('/conjugate', methods=['GET', 'POST'])
def home():
    verb_indicativo = None
    if request.method == "POST":
        received_verb = request.form.get("inputWord")
        conjugator = Conjugator(language='pt')
        verb = conjugator.conjugate(received_verb)

        verb_indicativo =   {
            "Verbo": received_verb,
            "Indicativo presente": verb["Indicativo"]["Indicativo presente"],
            "Indicativo preterito perfeito simples": verb["Indicativo"]["Indicativo pretérito perfeito simples"],
            "Indicativo preterito imperfeito": verb["Indicativo"]["Indicativo pretérito imperfeito"],
            "Indicativo futuro do presente": verb["Indicativo"]["Indicativo Futuro do Presente Simples"]
    }
        
    
    

    return render_template('conjugate.html', verb_indicativo=verb_indicativo)
 

@app.route('/conjugate/<clicked_verb>')
def conjugate(clicked_verb):
    conjugator = Conjugator(language='pt')
    verb = conjugator.conjugate(clicked_verb)

    verb_indicativo = {
        "Verbo": clicked_verb,
        "Indicativo presente": verb["Indicativo"]["Indicativo presente"],
        "Indicativo preterito perfeito simples": verb["Indicativo"]["Indicativo pretérito perfeito simples"],
        "Indicativo preterito imperfeito": verb["Indicativo"]["Indicativo pretérito imperfeito"],
        "Indicativo futuro do presente": verb["Indicativo"]["Indicativo Futuro do Presente Simples"]
    }

    return render_template('conjugate.html', verb_indicativo=verb_indicativo)


# conjug_manage = ConjugManager(language='pt')


@app.route("/json")
def send_json():
    data = verb_indicativo
    return json.dumps(data, ensure_ascii=False, indent=4)
# testing out how to send and get data to and from the server

# response = requests.get("http://localhost:5000/json")
# print(response.json())




# Trying to write the required conjugations to a json file
# So I can later send it to my website to be used in the conjugation table
# with open("falar_conjugs.json", "w", encoding="utf-8") as localfile:
#     json.dump(verb_indicativo, localfile, ensure_ascii=False, indent=4)

