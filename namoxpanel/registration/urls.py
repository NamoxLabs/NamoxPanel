# from django.urls import path
from django.contrib.auth import views as auth_views

from django.conf.urls import include, url
from django.contrib.auth import views as django_views

from . import views

# app_name = "accounts"
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^password/reset/$', views.password_reset,
        name='account_reset_password'),
    # url(r'^password/reset/done/$', django_views.password_reset_done,
    #     kwargs={'template_name': 'account/password_reset_done.html'},
    #     name='account_reset_password_done'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',  # noqa
        views.password_reset_confirm, name='account_reset_password_confirm'),
    # url(r'password/reset/complete/$', django_views.password_reset_complete,
    #     kwargs={'template_name': 'account/password_reset_from_key_done.html'},
    #     name='account_reset_password_complete'),
]
