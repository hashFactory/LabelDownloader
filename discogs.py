import discogs_client

# AUTHENTICATE DISCOGS CLIENT
# ----might switch to manual OAuth2 so that I don't have to relogin every
# ----...time I want to test something.
cons_key = 'XVCXsYXrAEMPCJQLTXtX'
cons_sec = 'xHxCHqhepTtkZMZIuoHtdFZAbMDNBUCF'

user_agent = 'Label2Spotify/1.0'

discogsclient = discogs_client.Client(user_agent)

discogsclient.set_consumer_key(cons_key, cons_sec)
token, secret, url = discogsclient.get_authorize_url()

print(f'Please browse to the following URL {url}')

accepted = 'n'
while accepted.lower() == 'n':
    print
    accepted = input(f'Have you authorized me at {url} [y/n] :')


# Waiting for user input. Here they must enter the verifier key that was
# provided at the unqiue URL generated above.
oauth_verifier = input('Verification code : ')

try:
    access_token, access_secret = discogsclient.get_access_token(oauth_verifier)
except HTTPError:
    print('Unable to authenticate.')
    sys.exit(1)

# fetch the identity object for the current logged in user.
user = discogsclient.identity()

#TESTING ONLY
import pickle
object = discogsclient
file = open('oauth_works.pickle', 'wb') 
pickle.dump(object, file)

results = discogsclient.search('Stockholm By Night', type='release')
print(results[0].artists[0])