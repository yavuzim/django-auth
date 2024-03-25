from django.urls import path
from profiller.api import views

urlpatterns = [
    path('kullanici-profilleri/', views.ProfilList.as_view(), name='profiller')
]