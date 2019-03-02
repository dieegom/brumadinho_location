from django.urls import path
from apps.missingpeople.views import missingpeople, createcsv

app_name = 'missingpeople'

urlpatterns = [
    path('missingpeople', missingpeople, name='missingpeople'),
    path('createcsv', createcsv, name='createcsv'),
]