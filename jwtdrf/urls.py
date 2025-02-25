from django.urls import path
from .views import Home


urlpatterns = [
    path('hello', Home.as_view()),
]
