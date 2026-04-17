from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.views.generic import TemplateView, View
from task.models import Task
from django.shortcuts import render



# class HomeView(View):
#     def get(self, request):
#         templates = loader.get_template('home.html')
#         return HttpResponse(templates.render())
#         # return HttpResponse("Hello, World!")
    

# class HomeView(TemplateView):
#     template_name = "home.html"

#     def get(self, request):
#         print(self.template_name)
#         return render(request, self.template_name)

class HomeView(View):
    def get(self, request):
        return render(request, "home.html")