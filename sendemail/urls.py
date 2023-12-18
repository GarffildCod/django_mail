from django.urls import include, path
from .views import *

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),
]
