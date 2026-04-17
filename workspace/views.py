from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import View

from task.models import Task
from .models import WorkSpace
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin



class WorkSpaceView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''
    def get(self, request):
        templates = loader.get_template('workspace.html')
        workspace = WorkSpace.objects.all()
        context = {
            'workspace': workspace,
        }
        return HttpResponse(templates.render(context, request))
    
class WorkSpaceCreateView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''
    def get(self, request):
        templates = loader.get_template('addworkspace.html')
        return HttpResponse(templates.render())
    
    def post(self, request):
        workspace = WorkSpace(name= request.POST.get('name'))
        workspace.save()
        return redirect('workspace')

class WorkSpaceDetailView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''
    def get(self, request, workspace_id):
        templates = loader.get_template('workspace_detail.html')
        workspace = WorkSpace.objects.get(id=workspace_id)
        tasks = Task.objects.filter(workspace=workspace)
        context = {
            'workspace': workspace,
            'tasks': tasks,
        }
        return HttpResponse(templates.render(context, request))
