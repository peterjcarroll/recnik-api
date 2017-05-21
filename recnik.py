import hug
import spell
from yawp.dict import serbocroatian

def cors_support(response, *args, **kwargs):
    response.set_header('Access-Control-Allow-Origin', '*')

@hug.get(requires=cors_support)
def suggest(search: hug.types.text):
    words = spell.candidates(search)
    is_word = len(spell.known([search])) > 0
    return {'is_word': is_word, 'words': words}

@hug.get(requires=cors_support, output=hug.output_format.text)
def lookup(word: hug.types.text): 
    return serbocroatian.get_json(word)