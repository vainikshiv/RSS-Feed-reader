from django.urls import path
from . import views

app_name='reader'

urlpatterns = [
    path('',views.home, name='home'),
    path('international/',views.international, name='international'),
    path('national/',views.national, name='national')
]
