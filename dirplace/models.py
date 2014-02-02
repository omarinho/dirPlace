from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.utils.encoding import smart_str, smart_unicode
from django.conf import settings
from django import forms as forms
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError
from djangoratings.fields import RatingField
from mptt.models import MPTTModel, TreeForeignKey
from userena.models import UserenaBaseProfile
from unidecode import unidecode
import datetime
import requests
import re
import string
import random
import os.path

def id_generator(size=9, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def userPicture_file_name(instance, filename):
    if not filename:
        return ""
    exts = re.search('[.]([^.]*)$',filename)
    if exts is None:
        ext  = ''
    else:
        ext = '.'+exts.group(1)
    return '/'.join(['uploaded/users/', str(instance.id), '/'+id_generator(27)+'%s' % (ext)])

def promotionPicture_file_name(instance, filename):
    if not filename:
        return ""
    exts = re.search('[.]([^.]*)$',filename)
    if exts is None:
        ext  = ''
    else:
        ext = '.'+exts.group(1)
    return '/'.join(['uploaded/promotions/', str(instance.id), '/'+id_generator(27)+'%s' % (ext)])

class UserProfile(UserenaBaseProfile):
    MARITAL_STATUSES = (
        ('SIN', 'Single'),
        ('MAR', 'Married'),
        ('SEP', 'Separated'),
        ('DIV', 'Divorced'),
        ('WID', 'Widowed'),
        ('COH', 'Cohabiting'),
    )
    GENRES = (
        ('FEM', 'Female'),
        ('MAL', 'Male'),
    )
    PRIVACY_OPTIONS = (
        ('open', 'Open'),
        ('registerd', 'Registered'),
        ('closed', 'Closed'),
    )
    user = models.OneToOneField(User,unique=True,verbose_name=_('user'),related_name='my_profile')
    birth_date = models.DateTimeField(null=True, blank=True)
    genre = models.CharField(max_length=3, choices=GENRES, null=True, blank=True)
    occupation = models.ForeignKey('Occupation', null=True, blank=True)
    marital_status = models.CharField(max_length=3, choices=MARITAL_STATUSES, null=True, blank=True)
    qrcode = models.CharField(max_length=36, null = True, blank=True)
    added_date = models.DateTimeField(null=True, blank=True)
    last_update = models.DateTimeField(null=True, blank=True)
    picture = models.ImageField(upload_to=userPicture_file_name, null=True, blank=True)
    def __unicode__(self):
        return self.user.email
    def save(self, *args, **kwargs):
        if self.id is not None:
            self.last_update = datetime.datetime.now()
        else:
            self.added_date = datetime.datetime.now()
            self.last_update = datetime.datetime.now()
        super(UserProfile, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"


class Occupation(models.Model):
    name = models.CharField(max_length=81)
    name_es = models.CharField(max_length=81)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = "Occupation"
        verbose_name_plural = "Occupations"
        ordering = ['name']

class Place(models.Model):
    name = models.CharField(max_length=243)
    category = models.ForeignKey('Category')
    description = models.TextField()
    address1 = models.CharField(max_length=243, null=True, blank=True)
    address2 = models.CharField(max_length=243, null=True, blank=True)
    zip = models.CharField(max_length=9, null=True, blank=True)
    city = models.CharField(max_length=81, null=True, blank=True)
    state = models.CharField(max_length=81, null=True, blank=True)
    country = models.ForeignKey('Country', null=True, blank=True)
    phone = models.CharField(max_length=81, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    website = models.CharField(max_length=243, null=True, blank=True)
    open_hours = models.CharField(max_length=255, null=True, blank=True)
    added_date = models.DateTimeField(null=True, blank=True)
    last_update = models.DateTimeField(null=True, blank=True)
    rating = RatingField(range=5)
    def __unicode__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.id is not None:
            self.last_update_date = datetime.datetime.now()
        else:
            self.added_date = datetime.datetime.now()
            self.last_update_date = datetime.datetime.now()
        super(Place, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "Place"
        verbose_name_plural = "Places"

class Category(MPTTModel):
    name = models.CharField(max_length=81)
    name_es = models.CharField(max_length=81)
    slug = models.CharField(max_length=255)
    slug_es = models.CharField(max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']
    class MPTTMeta:
        order_insertion_by = ['name']

class Country(models.Model):
    iso2 = models.CharField(max_length=2, null=True, blank=True)
    short_name = models.CharField(max_length=80)
    long_name = models.CharField(max_length=80)
    iso3 = models.CharField(max_length=3, null=True, blank=True)
    numcode = models.CharField(max_length=6, null=True, blank=True)
    un_member = models.CharField(max_length=12, null=True, blank=True)
    calling_code = models.CharField(max_length=8, null=True, blank=True)
    cctld = models.CharField(max_length=5, null=True, blank=True)
    short_name_es = models.CharField(max_length=80)
    long_name_es = models.CharField(max_length=80)
    def __unicode__(self):
        return self.short_name
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ['short_name']

class Resource(models.Model):
    RESOURCE_TYPES = (
        ('PIC', 'Picture'),
        ('VID', 'Video'),
        ('FIL', 'File'),
    )
    place = models.ForeignKey('Place')
    type = models.CharField(max_length=3, choices=RESOURCE_TYPES, null=True, blank=True)
    content = models.CharField(max_length=255, null=True, blank=True)
    def __unicode__(self):
        return self.id
    class Meta:
        verbose_name = "Resource"
        verbose_name_plural = "Resources"

class Promotion(models.Model):
    PROMOTION_TYPES = (
        ('DIS', 'Discount'),
        ('COU', 'Coupon'),
        ('OFF', 'Offer'),
    )
    USERS_AGES = (
        ('ALL', 'All fans'),
        ('3MO', 'People who have been fans since at least the last 3 months'),
        ('1YE', 'People who have been fans since at least the last 12 months'),
    )
    place = models.ForeignKey('Place')
    type = models.CharField(max_length=3, choices=PROMOTION_TYPES, null=True, blank=True)
    description = models.CharField(max_length=81)
    gift = models.CharField(max_length=243, null=True, blank=True)
    involved_products = models.TextField(null=True, blank=True)
    from_date = models.DateTimeField(null=True, blank=True)
    to_date = models.DateTimeField(null=True, blank=True)
    picture = models.ImageField(upload_to=promotionPicture_file_name, null=True, blank=True)
    users_age = models.CharField(max_length=3, choices=USERS_AGES, null=True, blank=True)
    restrictions = models.TextField()
    added_date = models.DateTimeField(null=True, blank=True)
    last_update = models.DateTimeField(null=True, blank=True)
    def save(self, *args, **kwargs):
        if self.id is not None:
            self.last_update_date = datetime.datetime.now()
        else:
            self.added_date = datetime.datetime.now()
            self.last_update_date = datetime.datetime.now()
        super(Promotion, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.description
    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"