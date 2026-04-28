from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import View
from django.contrib.auth.models import User
from task.models import Task
from todo.helper import is_owner, workspace_details, is_admin
from .models import WorkSpace
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin



class WorkSpaceView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''
    def get(self, request):
        user = self.request.user
        # workspace = WorkSpace.objects.filter(created_by=user) or WorkSpace.objects.filter(members=user)

        if is_admin(user):
            workspace = WorkSpace.objects.all()
        else:
            workspace = WorkSpace.objects.filter(members=user)
        # print(workspace)
        # workspace = WorkSpace.objects.all()
        context = {
            'workspace': workspace,
        }
        return render(request, 'workspace.html', context)
    
class WorkSpaceCreateView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''
    def get(self, request):
        return render(request, 'addworkspace.html')
    
    def post(self, request):
        current_user = self.request.user
        workspace = WorkSpace(
            name= request.POST.get('name'),
            created_by = current_user
            )
        
        workspace.save()

        workspace.members.set([current_user])

        workspace.save()
        return redirect('workspace')

class WorkSpaceDetailView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''
    def get(self, request, workspace_id):
        workspace = workspace_details(workspace_id)
        tasks = Task.objects.filter(workspace=workspace)
        context = {
            'workspace': workspace,
            'tasks': tasks,
        }
        return render(request, 'workspace_detail.html', context)

class AddMemberView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''

    def get(self, request, workspace_id):
        workspace = workspace_details(workspace_id)

        if(not is_owner(request.user, workspace)):
            return HttpResponse("You are not authorized to add members to this workspace.")
        
        users = User.objects.all()
        # print(users)
        # print(workspace)
        # print(workspace.members.all())
        members = workspace.members.all()
        users = [user for user in users if user not in members]
        context = {
            'workspace': workspace,
            'users': users,
            'members': members,
        }
        return render(request, 'add_member.html', context)
    
    def post(self, request, workspace_id):
        workspace = workspace_details(workspace_id)
        if not is_owner(request.user, workspace):
            return HttpResponse("You are not authorized to add members to this workspace.")
        username = request.POST.get('name')
        user = User.objects.get(username=username)
        workspace.members.add(user)
        return redirect('task', workspace_id=workspace_id)
    

class WorkSpaceDeleteView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''
    def get(self, request, workspace_id):
        workspace = workspace_details(workspace_id)
        if not is_owner(request.user, workspace):
            return HttpResponse("You are not authorized to delete this workspace.")
        context = {
            'workspace': workspace,
        }
        return render(request, 'deleteworkspace.html', context)
    
    def post(self, request, workspace_id):
        workspace = workspace_details(workspace_id)
        if not is_owner(request.user, workspace):
            return HttpResponse("You are not authorized to delete this workspace.")
        workspace.delete()
        return redirect('workspace')
    
class WorkSpaceUpdateView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''
    def get(self, request, workspace_id):
        workspace = workspace_details(workspace_id)
        if not is_owner(request.user, workspace):
            return HttpResponse("You are not authorized to update this workspace.")
        context = {
            'workspace': workspace,
        }
        return render(request, 'updateworkspace.html', context)
    
    def post(self, request, workspace_id):
        workspace = workspace_details(workspace_id)
        if not is_owner(request.user, workspace):
            return HttpResponse("You are not authorized to update this workspace.")
        workspace.name = request.POST.get('workspace')
        workspace.save()
        return redirect('workspace')