import requests
import json
import base64 

def getAccessToken():
    client_id = "a51cd24340f54db6b4feec53c54c16b9"
    client_secret = "c10f1dd816da40d8b62f8482b69c84b8"
    content_type = "application/x-www-form-urlencoded"
    SPOTIFY_URL_TOKEN = "https://accounts.spotify.com/api/token?grant_type=client_credentials"

    encoded = base64.urlsafe_b64encode("{}:{}".format(client_id, client_secret).encode()).decode()
    print("encoded: {}".format(encoded))

    headers = {
    'Content-Type': content_type,
    'Authorization': 'Basic {}'.format(encoded)
    }

    response = requests.request("POST", SPOTIFY_URL_TOKEN, headers=headers).json()
    
    print(json.dumps(response, indent=4))

    access_token = response['access_token']

    print("Access Token: {}".format(access_token))

    return access_token


#if __name__ == "__main__":
#    getAccessToken()
