from flask import Flask, render_template, request
from mlconjug3 import Conjugator
from mlconjug3 import ConjugManager 
# import os
import json




app = Flask(__name__)
conjugators = {
    'pt': Conjugator(language='pt'),
    'en': Conjugator(language='en')

}


# https://mlconjug3.readthedocs.io/en/latest/readme.html





# Conjugations for English speakers learning Portuguese

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/conjugate', methods=['GET', 'POST'])
def home():
    verb_indicativo = None
    if request.method == "POST":
        received_verb = request.form.get("inputWord")
        
        conjugator = conjugators['pt']
        verb = conjugator.conjugate(received_verb)

        indicativo = verb["Indicativo"]
        verb_indicativo =   {
            "Verbo": received_verb,
            "Indicativo presente": indicativo["Indicativo presente"],
            "Indicativo preterito perfeito simples": indicativo["Indicativo pretérito perfeito simples"],
            "Indicativo preterito imperfeito": indicativo["Indicativo pretérito imperfeito"],
            "Indicativo futuro do presente": indicativo["Indicativo Futuro do Presente Simples"]
    }
        
    
    

    return render_template('conjugate.html', verb_indicativo=verb_indicativo)
 

@app.route('/conjugate/<clicked_verb>')
def link(clicked_verb):
    conjugator = conjugators['pt']
    verb = conjugator.conjugate(clicked_verb)

    indicativo = verb["Indicativo"]
    verb_indicativo = {
        "Verbo": clicked_verb,
        "Indicativo presente": indicativo["Indicativo presente"],
        "Indicativo preterito perfeito simples": indicativo["Indicativo pretérito perfeito simples"],
        "Indicativo preterito imperfeito": indicativo["Indicativo pretérito imperfeito"],
        "Indicativo futuro do presente": indicativo["Indicativo Futuro do Presente Simples"]
    }

    return render_template('conjugate.html', verb_indicativo=verb_indicativo)





# Conjugations for Portuguese speakers learning English

@app.route('/pt')
def home_pt():
        
        return render_template('pt-index.html')

@app.route('/conjugar', methods=['GET', 'POST'])
def conjugate_pt():
     indicative_verb = None
     if request.method == "POST":
        received_verb = request.form.get("inputWord")
        
        conjugator = conjugators['en']
        verb = conjugator.conjugate(received_verb)

        indicative = verb["indicative"]
        indicative_verb =  {
             "Verbo": received_verb,
             "Indicativo presente": indicative["indicative present"],
             "Indicativo preterito perfeito simples": indicative["indicative past tense"],
             "Indicativo preterito imperfeito": indicative["indicative past tense"],
             "Indicativo futuro do presente": indicative["indicative present perfect"]
        }

        return render_template('pt-conjugate.html', indicative_verb=indicative_verb)


@app.route('/conjugar/<clicked_verb>')
def link_pt(clicked_verb):
    
    conjugator = conjugators['en']
    verb = conjugator.conjugate(clicked_verb)

    
    indicative = verb["indicative"]
    indicative_verb = {
        "Verbo": clicked_verb,
        "Indicativo presente": indicative["indicative present"],
        "Indicativo preterito perfeito simples": indicative["indicative past tense"],
        "Indicativo preterito imperfeito": indicative["indicative present continuous"],
        "Indicativo futuro do presente": indicative["indicative present perfect"]
    }

    return render_template('pt-conjugate.html', indicative_verb=indicative_verb)

if __name__ == '__main__':
    app.run(host='0.0.0.0')