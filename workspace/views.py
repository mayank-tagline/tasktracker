from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import View
from .models import WorkSpace
from django.shortcuts import redirect


class WorkSpaceView(View):
    def get(self, request):
        templates = loader.get_template('workspace.html')
        workspace = WorkSpace.objects.all()
        context = {
            'workspace': workspace,
        }
        return HttpResponse(templates.render(context, request))
    
class WorkSpaceCreateView(View):
    def get(self, request):
        templates = loader.get_template('addworkspace.html')
        return HttpResponse(templates.render())
    
    def post(self, request):
        workspace = WorkSpace(name= request.POST.get('name'))
        workspace.save()
        return redirect('workspace')

