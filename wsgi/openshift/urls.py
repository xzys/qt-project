from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^login/', 'market.views.login', name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', 'views.home', name='home'),
    
<<<<<<< HEAD
    url(r'^$', 'market.views.home', name='home'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
    url(r'^', 'market.views.home', name='home'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> a7136dc45ae003b282b07e21e962e7f8a5605b87
