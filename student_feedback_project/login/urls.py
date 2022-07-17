from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('registerParticipant/',views.registerParticipant,name='registerParticipant'),
]