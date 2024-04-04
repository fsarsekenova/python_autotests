
import requests
import pytest

Url='https://api.pokemonbattle.me/v2'
Token='9b6ba4ec983d1179eb0f2de36e4c6eaf'
Headers={'Content-Type':'application/json', 'trainer_token':'9b6ba4ec983d1179eb0f2de36e4c6eaf'}

def test_status_code():

    response=requests.get(url=f'{Url}/trainers', params ={'trainer_id' : 2331} )
    assert response.status_code==200

def test_part_of_response():
    response=requests.get(url=f'{Url}/trainers', params ={'trainer_id' : 2331} )
    assert response.json()['data'][0]['trainer_name']=='Kuza'