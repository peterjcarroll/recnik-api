import hug
import spell

@hug.get()
def suggest(search: hug.types.text):
    words = spell.candidates(search)
    is_word = len(spell.known([search]))>0
    return {'is_word': is_word, 'words': words}