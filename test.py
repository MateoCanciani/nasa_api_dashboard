
import requests
import re
import wikipedia 

apod_url="https://api.nasa.gov/planetary/apod?api_key=vR6zZ6UJloYcfESKfP2mpWKpZZ1wKqli8NW5BhwQ"

#Fonction compilant api_key + lien
def get_data(api_key) :
    apod_url=f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    response = requests.get(apod_url)
    print(response.json())
    url = response.json()['url']
    date = response.json()['date']
    explanation = response.json()["explanation"]
    title = response.json()["title"]
    #print(response.status_code)
    return response,url,date,explanation,title

api_key = "vR6zZ6UJloYcfESKfP2mpWKpZZ1wKqli8NW5BhwQ"
trait=("------------------------------------------------------------")
response,url,date,explanation,title = get_data(api_key)
print(f" Titre de l'image : {title} \n {trait} \n Date de l'image :  {date} \n {trait} \n Url de l'image : {url} \n {trait} \n Explication : {explanation} \n {trait} ")

"""
key_terms_list= re.findall(r'(?<!^)(?<!\. )[A-Z][a-z]+',explanation)
print(key_terms_list)
definitions={}
    for key_terms in key_terms_list :
    definitions[key_terms] = wikipedia.summary(wikipedia.suggest(key_terms))
print(definitions)

for key_term in key_terms_list:
    try :
        summary = wikipedia.summary(key_term)
        definitions[key_term] = summary
    except wikipedia.exceptions.DisambiguationError:
        definitions[key_term] = "NOPE"
    except wikipedia.exceptions.PageError:
        definitions[key_term] = "NOPE"
print(definitions)
"""


