from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up Spotify API credentials
client_id = '738cf140457540f592cddc50c06b7a26'
client_secret = 'bd94d538044f47d4bea8239792d83ebf'
redirect_uri = 'http://localhost:8000/callback'

# Create a SpotifyOAuth object with user-read-private and user-read-email scopes
sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=['user-library-read'])

# Get the authorization URL
auth_url = sp_oauth.get_authorize_url()

# Define a handler for the redirect URI
class CallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urlparse(self.path).query
        params = parse_qs(query)
        code = params['code'][0]
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Authorization code: ' + code.encode())

# Start a web server to listen for the redirect URI
server_address = ('', 8000)
httpd = HTTPServer(server_address, CallbackHandler)
print(f"Open this URL in your web browser: {auth_url}")
httpd.handle_request()

code = "https://accounts.spotify.com/authorize?client_id=738cf140457540f592cddc50c06b7a26&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fcallback&scope=user-library-read"
# Get the access token and refresh token using the authorization code
tokens = sp_oauth.get_access_token(code)

