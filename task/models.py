from django.db import models
from todo.mixins import CustomIDMixin
from workspace.models import WorkSpace


class Task(CustomIDMixin):
    task = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255, null=True)
    # pending, completed
    workspace = models.ForeignKey(WorkSpace, on_delete=models.CASCADE)
    


    def __str__(self):
        return f"{self.task} {self.description} {self.status} {self.workspace}"
