from mlconjug3 import Conjugator
from mlconjug3 import ConjugManager 
import os
import json


# https://mlconjug3.readthedocs.io/en/latest/readme.html


conjugator = Conjugator(language='pt')
conjug_manage = ConjugManager(language='pt')


# Getting the conjugations I want for the verb
# Later on verb will receive the user input from website
received_verb = "falar"
verb = conjugator.conjugate(received_verb)
# verb_indcativo_presente = verb["Indicativo"]["Indicativo presente"]

# verb_indicativo_perfeito = verb["Indicativo"]["Indicativo pretérito perfeito simples"] 

# verb_indicativo_imperfito = verb["Indicativo"]["Indicativo pretérito imperfeito"]

verb_indicativo = {
    "Verbo": received_verb,
    "Indicativo presente": verb["Indicativo"]["Indicativo presente"],
    "Indicativo preterito perfeito simples": verb["Indicativo"]["Indicativo pretérito perfeito simples"],
    "Indicativo preterito imperfeito": verb["Indicativo"]["Indicativo pretérito imperfeito"]
}




# Trying to write the required conjugations to a json file
# So I can later send it to my website to be used in the conjugation table
with open("falar_conjugs.json", "w", encoding="utf-8") as localfile:
    json.dump(verb_indicativo, localfile, ensure_ascii=False, indent=4)



# print(os.getcwd())
# basedir = os.path.abspath(os.path.dirname(__file__))
# falar_table_path = f"{basedir}/falar_table.json"

