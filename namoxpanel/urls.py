"""namoxpanel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.views import serve
#from django.views.i18n import javascript_catalog
from graphene_django.views import GraphQLView

#from .core.sitemaps import sitemaps
from .core.urls import urlpatterns as core_urls
from .registration.urls import urlpatterns as registration_urls
from .userprofile.urls import urlpatterns as userprofile_urls


urlpatterns = [
    url(r'^', include(core_urls)),
    url(r'^account/', include(registration_urls)),
    url(r'^graphql/', GraphQLView.as_view(graphiql=settings.DEBUG)),
    #url(r'^jsi18n/', javascript_catalog, name='javascript-catalog'),
    url(r'^profile/', include(userprofile_urls)),
]
