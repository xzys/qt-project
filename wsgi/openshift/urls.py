from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    

    url(r'^login/', 'market.views.login', name='login'),
    # url(r'^post/', 'market.views.login', name='login'),
    url(r'^home/', 'views.home', name='home'),
    url(r'^api/(?P<action>[_a-z]+)', 'market.views.api_request', name='api'),
    
    url(r'^(?P<category>[_a-z]+)', 'market.views.home', name='home'),
    url(r'^$', 'market.views.default', name='home'),
    
    url(r'^admin/', include(admin.site.urls)),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
