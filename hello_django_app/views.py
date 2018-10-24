from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self):
        data = {"message_title" : "Favorite Quote",
                "message": "If you do good, people will accuse you of selfish ulterior motives.Do good anyway."}
        return data
    
class AboutPageView (TemplateView):
    template_name = "resume.html"
    def get_context_data(self):
        data = {"message_title" : "WEBSITE",
                "message1": "Junior High School & Senior High School: Camarines Sur National High School",
                "message": "Elementary: Naga Central School 1"}
        return data

class ContactInfoPageView (TemplateView):
    template_name = "contactInfo.html"
    def get_context_data(self):
        data = {"message_title" : "Marey Klarize Sevilla ",
                "message1": "Address: Bagumbayan Naga City",
                "message2": "Email: mrysvlla@gmail.com",               
                "message3": "Mobile No. 09076741932"}
        return data

