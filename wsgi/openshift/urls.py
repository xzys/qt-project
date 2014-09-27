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
<<<<<<< HEAD
    url(r'^$', 'market.views.home', name='home'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
    url(r'^api/(?P<action>[_a-z]+)', 'market.views.get_json', name='api'),
    
    url(r'^$', 'market.views.home', name='home'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> 6357bb98854c762800bf739be7e272abfb933f4d
