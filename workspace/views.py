from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import View
from django.contrib.auth.models import User
from task.models import Task
from .models import WorkSpace
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin



class WorkSpaceView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''
    def get(self, request):
        templates = loader.get_template('workspace.html')
        user = self.request.user
        workspace = WorkSpace.objects.filter(created_by=user) | WorkSpace.objects.filter(members=user)
        # workspace = WorkSpace.objects.all()
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
        current_user = self.request.user
        print(current_user)
        user = User.objects.get(id=current_user.id)
        workspace = WorkSpace(
            name= request.POST.get('name'),
            created_by = current_user
            )
        workspace.members.add(user)
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

class AddMemberView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''

    def get(self, request, workspace_id):

        if(request.user != WorkSpace.objects.get(id=workspace_id).created_by):
            return HttpResponse("You are not authorized to add members to this workspace.")
        templates = loader.get_template('add_member.html')
        workspace = WorkSpace.objects.get(id=workspace_id)
        
        users = User.objects.all()
        # print(users)
        # print(workspace)
        # print(workspace.members.all())
        context = {
            'workspace': workspace,
            'users': users,
        }
        return HttpResponse(templates.render(context, request))
    
    def post(self, request, workspace_id):
        if(request.user != WorkSpace.objects.get(id=workspace_id).created_by):
            return HttpResponse("You are not authorized to add members to this workspace.")
        workspace = WorkSpace.objects.get(id=workspace_id)
        username = request.POST.get('name')
        user = User.objects.get(username=username)
        workspace.members.add(user)
        return redirect('workspace-detail', workspace_id=workspace_id)