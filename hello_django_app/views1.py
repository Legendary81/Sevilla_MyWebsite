from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self):
        data = {"message_title" : "aaa!",
                "message": "wew!"}
        return data
    
class AboutPageView (TemplateView):
    template_name = "about.html"
    def get_context_data(self):
        data = {"message_title" : "wao!",
                "message": "club !"}
        return data
    

