from django.urls import path,include
from .views import home_page_view

urlpatterns = [
    
    path("", home_page_view, name="home" ),
]


# please check if this two files are correct or not
# one is this view..py and other is urls.py