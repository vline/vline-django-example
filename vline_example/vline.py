import jwt
import time

# replace with values from your service settings
# see: https://vline.com/developer/docs/authentication
API_SECRET = 'YOUR_SECRET'
SERVICE_ID = 'YOUR_SERVICE_ID'
SESSION_EXPIRATION_TIME = 48 * 60 * 60 # 2 days in seconds

def create_auth_token(userId):
    # jwt payload
    payload = {
        "sub" : SERVICE_ID + ":" + str(userId),
        "iss" : SERVICE_ID,
        "exp" : time.time() + SESSION_EXPIRATION_TIME
    }
    # encode and sign token
    api_secret_key = jwt.base64url_decode(API_SECRET)
    return jwt.encode(payload, api_secret_key);

def create_user_profile(user):
    if user.last_name or user.first_name: 
        display_name = user.get_full_name()
    else:
        display_name = user.get_username()
    return {
        "id": user.id,
        "displayName": display_name
    }
