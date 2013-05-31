from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import vline

@login_required
def home(request, template='home.html'):
    #calendar = get_object_or_404(Calendar, slug=calendar_slug)
    if request.user.is_authenticated():
        users = map(vline.create_user_profile, User.objects.all())
    else:
        users = None
    return render_to_response(template, {
        "users": users,
    }, context_instance=RequestContext(request))