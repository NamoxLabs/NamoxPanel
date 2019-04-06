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
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.views import serve
from graphene_django.views import GraphQLView

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from namoxpanel.account import api_view as users_api
# from namoxpanel.apps import api_view as apps_api

#from .core.urls import urlpatterns as core_urls
#from .registration.urls import urlpatterns as user_account_urls
#from .userprofile.urls import urlpatterns as userprofile_urls
#from .graphicsdb.urls import urlpatterns as projects_urls
#from .apps.urls import urlpatterns as apps_urls

# router = DefaultRouter()
# router.register(r'', )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/register/', users_api.RegisterUsers.as_view(), name='auth-register'),
    url(r'^api-token-auth', obtain_jwt_token, name='create-token'),
    url(r'^api-token-refresh', refresh_jwt_token, name='refresh-token'),
    url(r'^api-token-verify', verify_jwt_token, name='verify-token'),
    #path('api/v1', include(router.urls)),

    #url(r'^apps/',
    #    include((apps_urls, 'apps'), namespace='apps')),
    #url(r'^account/',
    #    include((user_account_urls, 'account'), namespace='account')),
    #url(r'^', include(core_urls)),
]
