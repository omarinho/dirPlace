from django.core.context_processors import request
from django.core.files.images import get_image_dimensions
from django.shortcuts import render_to_response, redirect
from django.template.context import Context, RequestContext
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.sites.models import Site
from django.db.models import Max
from django.db import connection, transaction
from django.conf import settings
from dirplace.models import *
from dirplace.forms import *
from templated_email import send_templated_mail
from array import *
from cStringIO import StringIO
from tokenize import generate_tokens
from time import strftime, strptime
from random import randrange
from userena import views as userena_views
import datetime
import json
import requests
import urlparse
import urllib
import string
import random

def search_results(request):
    c = {}
    return render_to_response ('dirplace/search-results.html', c, context_instance =  RequestContext(request),)

def search_by_category(request, category_slug):
    theCategory = Category.objects.get(slug=category_slug);
    subCategories = Category.objects.filter(parent_id=theCategory.id)
    c = {
            'theCategory':theCategory,
            'subCategories':subCategories,
    }
    return render_to_response ('dirplace/search-by-category.html', c, context_instance =  RequestContext(request),)

def search_by_subCategory(request, category_slug, subCategory_slug):
    theCategory = Category.objects.get(slug=category_slug);
    theSubCategory = Category.objects.get(slug=subCategory_slug);
    tags = Category.objects.filter(parent_id=theSubCategory.id)
    c = {
            'theCategory':theCategory,
            'theSubCategory':theSubCategory,
            'tags':tags,
    }
    return render_to_response ('dirplace/search-by-subCategory.html', c, context_instance =  RequestContext(request),)

def search_by_tag(request, category_slug, subCategory_slug, tag_slug):
    theCategory = Category.objects.get(slug=category_slug);
    theSubCategory = Category.objects.get(slug=subCategory_slug);
    theTag = Category.objects.get(slug=tag_slug);
    c = {
            'theCategory':theCategory,
            'theSubCategory':theSubCategory,
            'theTag':theTag,
    }
    return render_to_response ('dirplace/search-by-tag.html', c, context_instance =  RequestContext(request),)

def about_us(request):
    c = {}
    return render_to_response ('dirplace/about-us.html', c, context_instance =  RequestContext(request),)

def faqs(request):
    c = {}
    return render_to_response ('dirplace/faqs.html', c, context_instance =  RequestContext(request),)

def terms_and_conditions(request):
    c = {}
    return render_to_response ('dirplace/terms-and-conditions.html', c, context_instance =  RequestContext(request),)

def privacy_policy(request):
    c = {}
    return render_to_response ('dirplace/privacy-policy.html', c, context_instance =  RequestContext(request),)

def get_add_for_android(request):
    c = {}
    return render_to_response ('dirplace/get-add-for-android.html', c, context_instance =  RequestContext(request),)

def contact(request):
    EMAIL_CUSTOMER_ATTENDANT  = getattr(settings, 'EMAIL_CUSTOMER_ATTENDANT', 'omar@dirplace.com')
    DEFAULT_FROM_EMAIL = getattr(settings, 'DEFAULT_FROM_EMAIL', 'info@dirplace.com')
    DOMAINURL = getattr(settings, 'DOMAINURL', 'http://dirplace.com/')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = 'Please reply to: ' + cd['email'] + '\n\n\n'
            message = message + cd['description']
            send_templated_mail(
                    template_name='contact-notification',
                    from_email=DEFAULT_FROM_EMAIL,
                    recipient_list=[EMAIL_CUSTOMER_ATTENDANT],
                    context={
                        'message':message,
                    },
            )
            return redirect('/dirplace/contact_thanks/')
    else:
        form = ContactForm()
    c = {
            'form': form
    }
    return render_to_response ('dirplace/contact-us.html', c, context_instance =  RequestContext(request),)

def contact_thanks(request):
    c = {}
    return render_to_response ('dirplace/contact_thanks.html', c, context_instance =  RequestContext(request),)

def editProfile(request, username):
    theUser = User.objects.get(username=username);
    theUserProfile = UserProfile.objects.get(user_id=theUser.id);
    successMessage = False
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            theUser.first_name = cd["first_name"]
            theUser.last_name = cd["last_name"]
            theUser.save()
            if request.POST.get('mugshot-clear', False):
                theUserProfile.mugshot = None
            else:
                if cd["mugshot"]:
                    theUserProfile.mugshot = cd["mugshot"]
            theUserProfile.birth_date = cd["birth_date"]
            theUserProfile.genre = cd["genre"]
            theUserProfile.occupation = cd["occupation"]
            theUserProfile.marital_status = cd["marital_status"]
            theUserProfile.save()
            successMessage = True
            form = EditProfileForm(initial={
                                        'first_name':theUser.first_name,
                                        'last_name':theUser.last_name,
                                        'mugshot':theUserProfile.mugshot,
                                        'birth_date':theUserProfile.birth_date,
                                        'genre':theUserProfile.genre,
                                        'occupation': theUserProfile.occupation,
                                        'marital_status': theUserProfile.marital_status,
                                    }
                            )
    else:
        form = EditProfileForm(initial={
                                        'first_name':theUser.first_name,
                                        'last_name':theUser.last_name,
                                        'mugshot':theUserProfile.mugshot,
                                        'birth_date':theUserProfile.birth_date,
                                        'genre':theUserProfile.genre,
                                        'occupation': theUserProfile.occupation,
                                        'marital_status': theUserProfile.marital_status,
                                    }
                            )

    c = {
            'username':username,
            'theUser':theUser,
            'theUserProfile':theUserProfile,
            'form': form,
            'successMessage': successMessage,
        }
    return render_to_response ('dirplace/edit_profile.html', c, context_instance =  RequestContext(request),)


