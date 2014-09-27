from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pimarket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/', 'market.views.login', name="login"),
    url(r'^', 'market.views.home',name="home"),
    url(r'^admin/', include(admin.site.urls)),
)

