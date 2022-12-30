import requests
import json
from access_token import *

url = ('https://api.spotify.com/v1/search?q=metallica&type=artist')

url_2 = ('https://api.spotify.com/v1/artists/1vCWHaC5f2uS3yhpwWbIA6/albums?album_type=SINGLE&offset=20&limit=10')

url_3 = ('https://api.spotify.com/v1/browse/new-releases')

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(getAccessToken())
}

response = requests.request("GET", url_3, headers=headers)
print(json.dumps(response.json(), indent=4))

# access_token = response['access_token']
test = response.json()['albums']['items'][0]["id"]

print(test)

jsonString = json.dumps(response.json())
jsonFile = open("new_release.json", "w")
jsonFile.write(jsonString)
jsonFile.close()


