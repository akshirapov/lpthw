

def scan(phrase: str):

    sentence = []

    words = phrase.strip().split()
    for word in words:
        word_type = get_type(word)
        sentence.append(word_type)

    return sentence


def get_type(word):

    token = 'error'
    if is_direction(word):
        token = 'direction'
    elif is_verb(word):
        token = 'verb'
    elif is_stop(word):
        token = 'stop'
    elif is_noun(word):
        token = 'noun'
    elif is_number(word):
        token = 'number'
        word = int(word)

    return token, word


def is_direction(word):
    directions = [
        'north',
        'south',
        'east',
        'west',
        'down',
        'up',
        'left',
        'right',
        'back'
    ]
    return word.lower() in directions


def is_verb(word):
    verbs = [
    'go',
    'stop',
    'kill',
    'eat',
    'jump'
    ]
    return word.lower() in verbs


def is_stop(word):
    stops = [
        'the',
        'in',
        'of',
        'from',
        'at',
        'it'
    ]
    return word.lower() in stops


def is_noun(word):
    nouns = [
    'door',
    'bear',
    'princess',
    'cabinet'
    ]
    return word.lower() in nouns


def is_number(word):
    try:
        int(word)
        return True
    except ValueError:
        return False