from flask import Flask, redirect, render_template, request
import requests
import base64



app = Flask(__name__)

#  Client Keys
CLIENT_ID = "a51cd24340f54db6b4feec53c54c16b9"
CLIENT_SECRET = "c10f1dd816da40d8b62f8482b69c84b8"
# Encoding values for header
ENCODED_CLIENT_SECRET = base64.b64encode(b'a51cd24340f54db6b4feec53c54c16b9:c10f1dd816da40d8b62f8482b69c84b8')
ENCODED_CLIENT_SECRET=ENCODED_CLIENT_SECRET.decode("utf-8")

# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"

# Server-side Parameters
REDIRECT_URI = "https://ed-5046562708520960.educative.run/callback"
SCOPE = "playlist-read-collaborative playlist-modify-public playlist-modify-private playlist-read-private user-library-read user-library-modify"
RESPONSE_TYPE = "code"
GRANT_TYPE = 'authorization_code'

@app.route("/")
def index():
    authorize_url = 'https://accounts.spotify.com/en/authorize?response_type={}&client_id={}&redirect_uri={}&scope={}&show_dialog=TRUE'.format(RESPONSE_TYPE,CLIENT_ID,REDIRECT_URI,SCOPE)
    response = redirect(authorize_url)
    return response


@app.route("/callback")
def callback():
    token_url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic '+'{}'.format(ENCODED_CLIENT_SECRET)
        }
    body = {'code': request.args.get('code'), 'redirect_uri': REDIRECT_URI, 
            'grant_type': GRANT_TYPE}
    post_response = requests.post(token_url,headers=headers,data=body)
    return render_template('home.html',token=post_response.json())


if __name__ == '__main__':
    app.run(debug=True)