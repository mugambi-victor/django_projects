from django.urls import path
from .views import submit_form

urlpatterns = [
    path('api/', submit_form, name='api'),
]
