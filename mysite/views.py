from django.core.context_processors import request
from django.shortcuts import render_to_response
from django.template.context import Context, RequestContext
from django.conf import settings
from dirplace.models import *

def home(request):
    mainCategories = Category.objects.filter(parent_id=None).order_by('name')
    c = {
            'mainCategories':mainCategories,
    }
    return render_to_response ('index.html', c, context_instance =  RequestContext(request),)

def close_window(request):
    c = {}
    return render_to_response ('close_window.html', c, context_instance =  RequestContext(request),)