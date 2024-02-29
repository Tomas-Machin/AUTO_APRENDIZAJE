<<<<<<< HEAD
import urllib.request, urllib.parse, urllib.error
import oauth  # descargar
import hidden

def augment(url, parameters):
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['consumer_key'], secrets['consumer_secret'])
    token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])

    oauth_request == oauth.OAuthRequest.from_consumer_and_token(consumer, token = token, http_method = 'GET', http_url = url, parameters = parameters)
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),  consumer, token)

=======
import urllib.request, urllib.parse, urllib.error
import oauth  # descargar
import hidden

def augment(url, parameters):
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['consumer_key'], secrets['consumer_secret'])
    token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])

    oauth_request == oauth.OAuthRequest.from_consumer_and_token(consumer, token = token, http_method = 'GET', http_url = url, parameters = parameters)
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),  consumer, token)

>>>>>>> 70eeabf7fe0392c3aa721948c166730523aa1e3e
    return oauth_request.to_url()