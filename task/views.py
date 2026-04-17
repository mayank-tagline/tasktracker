from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import View
from .models import Task
from workspace.models import WorkSpace
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin



# def (request):
#     templates = loader.get_template('task.html')
#     return HttpResponse(templates.render())

class TaskView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''
    def get(self, request):
        templates = loader.get_template('task.html')
        task = Task.objects.all()
        context = {
            'task': task,
        }
        return HttpResponse(templates.render(context, request))
    
class TaskCreateView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''
    def get(self, request):
        workspace = WorkSpace.objects.all()
        context = {
            'workspace': workspace,
        }
        templates = loader.get_template('addtask.html')
        return HttpResponse(templates.render(context, request))
    
    def post(self, request):
        ws =request.POST.get('workspace')
        workspace = WorkSpace.objects.get(id = ws)
        current_user = self.request.user

        print(current_user)

        task = Task(
            task= request.POST.get('task'),
            description=request.POST.get('description'),
            status="Pending",
            workspace=workspace,
            created_by = current_user
            )
        task.save()
        return redirect('task')

