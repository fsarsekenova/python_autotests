
import requests

Url='https://api.pokemonbattle.me/v2/'
Token='9b6ba4ec983d1179eb0f2de36e4c6eaf'
Headers={'Content-Type':'application/json', 'trainer_token':'9b6ba4ec983d1179eb0f2de36e4c6eaf'}
         
         

Body={  
    "name": "Бульбуль",
    "photo": "https://dolnikov.ru/pokemons/albums/003.png"
}
response=requests.post(url=f'{Url}pokemons',headers=Headers, json=Body)

print(response.text)
#"id":"15709"

Body_name={
    "pokemon_id": "15717",
    "name": "Булька",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
response_name=requests.put(url=f'{Url}pokemons',headers=Headers, json=Body_name)
print(response_name.text)
#"id":"15717"

Body_pokeball={
    "pokemon_id": "15717"
}
response_pokeball=requests.post(url=f'{Url}trainers/add_pokeball',headers=Headers, json=Body_pokeball)
print(response_pokeball.text)