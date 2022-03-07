import requests

TIBIADATA_API = 'https://api.tibiadata.com/v3/'


def online_players(guild_name):
    r = requests.get(TIBIADATA_API+'guild/{}'.format(guild_name.replace(' ', '+')))
    members = r.json().get('guilds').get('guild').get('members')
    online_members = [member for member in members if member.get('status') == 'online']
    return online_members

def all_players(guild_name):
    r = requests.get(TIBIADATA_API+'guild/{}'.format(guild_name.replace(' ', '+')))
    members = r.json().get('guilds').get('guild').get('members')
    return members

def get_dict_from_array(array, item, value):
    return next(x for x in array if x[item] == value)
