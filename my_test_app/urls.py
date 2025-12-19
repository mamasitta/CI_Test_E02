
from django.urls import path
from .views import home

app_name = 'my-test-app'
urlpatterns = [
    path('', home, name='home'),
]