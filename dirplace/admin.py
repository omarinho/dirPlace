from dirplace.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.contrib.admin.widgets import AdminFileWidget
from django.http import HttpResponse
from django import forms
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin

class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name','name_es',)
    mptt_level_indent = 20
admin.site.register(Category, CategoryAdmin)

admin.site.register(Country)
admin.site.register(Occupation)
admin.site.register(Place)
admin.site.register(Promotion)
admin.site.register(Resource)
admin.site.unregister(Site)

