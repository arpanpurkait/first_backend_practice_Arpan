from django.urls import path,include
from .views import home_page_view
from .views import about_page_view

urlpatterns = [
    
    path("", home_page_view, name="home" ),
    path("about/", about_page_view, name="about")
]


# please check if this two files are correct or not
# one is this view..py and other is urls.py