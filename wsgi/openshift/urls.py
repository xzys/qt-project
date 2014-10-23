from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

# admin.autodiscover()
urlpatterns = patterns('',
    url(r'^admin[/]?', include(admin.site.urls)),
    url(r'^logout[/]?', 'market.views.request_log_out', name='request_log_out'),
    url(r'^profile[/]?','market.views.request_profile', name='request_profile'),
    url(r'^authrequest/(?P<authtype>(login|register))','market.views.handler_user_auth_request',name='handler_user_auth_request'),
    url(r'^login[/]?', 'market.views.login', name='login'),
    url(r'^post[/]?', 'market.views.post', name='post'),
    url(r'^home[/]?', 'views.home', name='home'),
    url(r'^api/(?P<action>[_a-z]+)', 'market.views.api_request', name='api'),
    url(r'^(?P<category>[_a-z]+)[/]?', 'market.views.home', name='home'),
    
    
    url(r'^$', 'market.views.default', name='home'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
