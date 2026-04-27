from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import View
from .models import Task
from workspace.models import WorkSpace
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from todo.helper import is_user_in_workspace, workspace_details, workspace_tasks, task_details



# def (request):
#     templates = loader.get_template('task.html')
#     return HttpResponse(templates.render())

class TaskView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''
    def get(self, request, workspace_id):
        workspace = workspace_details(workspace_id)
        if workspace is None:
            return redirect('workspace')
        if not is_user_in_workspace(self.request.user, workspace):
            return redirect('workspace')
        templates = loader.get_template('task.html')
        task = workspace_tasks(workspace)
        context = {
            'task': task,
            'workspace': workspace
        }
        return HttpResponse(templates.render(context, request))
    
class TaskCreateView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''
    def get(self, request, workspace_id):
        workspace = workspace_details(workspace_id)
        if workspace is None:
            return redirect('workspace')
        context = {
            'workspace': workspace,
        }
        templates = loader.get_template('addtask.html')
        return HttpResponse(templates.render(context, request))
    
    def post(self, request, workspace_id):
        workspace = workspace_details(workspace_id)
        if workspace is None:
            return redirect('workspace')
        current_user = self.request.user

        # print(current_user)

        task = Task(
            task= request.POST.get('task'),
            description=request.POST.get('description'),
            status="pending",
            workspace=workspace,
            created_by = current_user
            )
        task.save()
        return redirect('task' , workspace_id=workspace_id)

class TaskDeleteView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''
    def get(self, request, workspace_id, task_id):
        workspace = workspace_details(workspace_id)
        if workspace is None:
            return redirect('workspace')
        if not is_user_in_workspace(self.request.user, workspace):
            return redirect('task' , workspace_id=workspace_id)
        task = task_details(task_id)
        if task is None:
            return redirect('task' , workspace_id=workspace_id)
        context = {
            'workspace': workspace,
            'task': task
        }
        templates = loader.get_template('deletetask.html')
        return HttpResponse(templates.render(context, request))
    def post(self, request, workspace_id, task_id):
        task = task_details(task_id)
        if task is None:
            return redirect('task' , workspace_id=workspace_id)
        task.delete()
        return redirect('task' , workspace_id=workspace_id)
    

class TaskUpdateView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''
    def get(self, request, workspace_id, task_id):
        workspace = workspace_details(workspace_id)
        if workspace is None:
            return redirect('task' , workspace_id=workspace_id)
        if not is_user_in_workspace(self.request.user, workspace):
            return redirect('workspace')
        
        # print(workspace.members.all())

        # for member in workspace.members.all():
        #     if self.request.user != member:
        #         return redirect('workspace')
        # if self.request.user not in workspace.members.all():
        #     return redirect('workspace')
        task = task_details(task_id)
        if task is None:
            return redirect('task' , workspace_id=workspace_id)
        context = {
            'workspace': workspace,
            'task': task
        }
        templates = loader.get_template('updatetask.html')
        return HttpResponse(templates.render(context, request))
    
    def post(self, request, workspace_id, task_id):
        task = task_details(task_id)
        if task is None:
            return redirect('task', workspace_id=workspace_id)
        if request.POST.get('task') =="":
            return redirect('update-task' , workspace_id=workspace_id, task_id=task_id)
        task.task = request.POST.get('task')
        task.description = request.POST.get('description')
        if request.POST.get('status') == 'completed':
            task.completed_by = self.request.user
        if request.POST.get('status') == 'pending':
            task.completed_by = None
        task.status = request.POST.get('status')
        task.save()
        return redirect('task' , workspace_id=workspace_id)