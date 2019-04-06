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
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.views import serve
from graphene_django.views import GraphQLView

from .core.urls import urlpatterns as core_urls
from .registration.urls import urlpatterns as user_account_urls
from .userprofile.urls import urlpatterns as userprofile_urls
from .graphicsdb.urls import urlpatterns as projects_urls
from .apps.urls import urlpatterns as apps_urls

urlpatterns = [
    url(r'^apps/',  
        include((apps_urls, 'apps'), namespace='apps')),
    #url(r'^account/', include('.userprofile.urls')),
    url(r'^account/',  
        include((user_account_urls, 'account'), namespace='account')),
    # url(r'^profile/', include(userprofile_urls)),
    # url( r'^projects/', include(projects_urls)),
    url(r'^', include(core_urls)),
    #url(r'^graphql/', GraphQLView.as_view(graphiql=settings.DEBUG)),
]
