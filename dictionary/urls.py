from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import home, all_words

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', home),
    url(r'^$', home),
    url(r'^words/$', all_words),
)
