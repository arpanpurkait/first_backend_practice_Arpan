from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def home_page_view(request): # new
    context = {
        "inventory_list": ["laptop", "desktop", "smartphone", "tablet"],
        "greeting": "THank You foR visitING. !",

    }
    return render(request, "home.html",context)

class AboutPageView(TemplateView): # new
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "829-369-0911"
        return context