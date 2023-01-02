from django.urls import path

from .views import basmalaviews

app_name = 'basmala'
urlpatterns = [
    path('list/', basmalaviews, name='basmalaList')
]