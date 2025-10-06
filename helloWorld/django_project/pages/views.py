from django.shortcuts import render
from django.http import HttpResponse
def home_page_view(request):
    return HttpResponse("Home Page")


def about_page_view(request):
    context = {
        "name": "Arpan",
        "age": 21
    }
    return render(request,"pages/about.html",context)


# hey I am testing the git ....
# is this working...?

# kya ye kaam kar rah hai?
