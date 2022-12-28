from django.urls import path
from app2.views import *
app_name = "any name"

urlpatterns = [
    path("first/", first, name="first"),
]
