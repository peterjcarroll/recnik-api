import hug
import spell

def cors_support(response, *args, **kwargs):
    response.set_header('Access-Control-Allow-Origin', '*')

@hug.get(requires=cors_support)
def suggest(search: hug.types.text):
    words = spell.candidates(search)
    is_word = len(spell.known([search]))>0
    return {'is_word': is_word, 'words': words}