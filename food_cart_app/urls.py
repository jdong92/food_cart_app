from django.conf.urls import patterns, include, url
from django.contrib import admin
from signup import urls
from django.views.generic import TemplateView


urlpatterns = [
    # Examples:
    # url(r'^$', 'food_cart_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('login.urls')),
    url(r'^signup/', include('signup.urls'))
]
