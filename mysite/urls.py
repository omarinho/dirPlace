from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mysite.views.home', name='home'),
    url(r'^close_window/$', 'mysite.views.close_window'),
    url(r'^accounts/(?P<username>[\w_-]+)/edit/$', 'dirplace.views.editProfile',name= 'userena_profile_edit'),
    url(r'^search-results/$', 'dirplace.views.search_results'),
    url(r'^categories/(?P<category_slug>[\w_-]+)/$', 'dirplace.views.search_by_category'),
    url(r'^categories/(?P<category_slug>[\w_-]+)/(?P<subCategory_slug>[\w_-]+)/$', 'dirplace.views.search_by_subCategory'),
    url(r'^categories/(?P<category_slug>[\w_-]+)/(?P<subCategory_slug>[\w_-]+)/(?P<tag_slug>[\w_-]+)/$', 'dirplace.views.search_by_tag'),
    url(r'^about-us/$', 'dirplace.views.about_us'),
    url(r'^faqs/$', 'dirplace.views.faqs'),
    url(r'^contact-us/$', 'dirplace.views.contact'),
    url(r'^contact_thanks/', 'dirplace.views.contact_thanks'),
    url(r'^terms-and-conditions/$', 'dirplace.views.terms_and_conditions'),
    url(r'^privacy-policy/$', 'dirplace.views.privacy_policy'),
    url(r'^get-add-for-android/$', 'dirplace.views.get_add_for_android'),
    (r'^accounts/', include('userena.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/media'}),
    url(r'^captcha/', include('captcha.urls')),
)