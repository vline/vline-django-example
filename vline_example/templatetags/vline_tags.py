from django import template
from .. import vline
import json

def vline_service_id():
    return "'" + vline.SERVICE_ID + "'"
    
def vline_auth_token(user):
    return "'" + vline.create_auth_token(user.id) + "'"

def vline_user_profile(user):
    return json.dumps(vline.create_user_profile(user))
    
register = template.Library()
register.simple_tag(vline_service_id)
register.filter("vline_auth_token", vline_auth_token)
register.filter("vline_user_profile", vline_user_profile)
