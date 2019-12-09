from django.urls import path
from .views import *

urlpatterns=[
    path('',formview,name='formv'),
]
