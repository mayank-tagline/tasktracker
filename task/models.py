from django.db import models
from todo.mixins import CustomIDMixin
from workspace.models import WorkSpace
from django.contrib.auth.models import User



class Task(CustomIDMixin):
    task = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255, null=True)
    # pending, completed
    workspace = models.ForeignKey(WorkSpace, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE , related_name='task_created_by', null= True)
    completed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_completed_by',null=True)

    def __str__(self):
        return f"{self.task} - {self.status}"
