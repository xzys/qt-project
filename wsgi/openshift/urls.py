from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'market.views.login', name='login'),
    url(r'^home/', 'views.home', name='home'),
    url(r'^api/(?P<action>[_a-z]+)', 'market.views.get_json', name='api'),
    
    url(r'^(?P<category>[_a-z]+)', 'market.views.home', name='home'),
    url(r'^$', 'market.views.default', name='home'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)