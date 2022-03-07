import requests

TIBIADATA_API = 'https://api.tibiadata.com/v3/'

def check_player(player_name):
    r = requests.get(TIBIADATA_API+'character/{}'.format(player_name.replace(' ', '+')))
    return r.json().get('characters')


def check_player_name(player_name):
    character = check_player(player_name)
    return character.get('character').get('name')
