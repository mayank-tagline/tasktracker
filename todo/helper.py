from workspace.models import WorkSpace
from task.models import Task
from account.models import User

def is_user_in_workspace(user, workspace):
    if workspace.members.filter(id=user.id).exists():
        return True
    if user.is_staff:
        return True
    return False

def is_admin(user):
    if user.is_staff:
        return True
    return False

def workspace_details(workspace_id):
    try:
        workspace = WorkSpace.objects.get(id=workspace_id)
        return workspace
    except WorkSpace.DoesNotExist:
        return None
    
def workspace_tasks(workspace):
    try:
        tasks= Task.objects.filter(workspace=workspace)
        return tasks
    except Task.DoesNotExist:
        return None
    
def task_details(task_id):
    try:
        task = Task.objects.get(id=task_id)
        return task
    except Task.DoesNotExist:
        return None
    

def is_owner(user, workspace):
    if workspace.created_by == user:
        return True
    if user.is_staff:
        return True
    return False