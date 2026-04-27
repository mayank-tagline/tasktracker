from workspace.models import WorkSpace
from task.models import Task
from account.models import User

def is_user_in_workspace(user, workspace):
    if workspace.members.filter(id=user.id).exists():
        return True
    if user.is_staff:
        return True
    return False