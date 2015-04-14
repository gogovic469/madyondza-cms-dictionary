from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/$', include(admin.site.urls)),
    url(r'', views.home),
    url(r'^home/$', views.home),
)
