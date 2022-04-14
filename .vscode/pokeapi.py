import requests

def get_pokemon_info(poke_name):
    #print("Getting Pokemon information...", end="")+str(poke_name)
    URL = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(URL)
    if response.status_code == 200:
        print("success!")
        return response.json()
    else:
        print("failed. Response code",response.status_code)
        return
