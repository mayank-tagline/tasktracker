from django.db import models
from todo.mixins import CustomIDMixin
from django.contrib.auth.models import User


class WorkSpace(CustomIDMixin):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey( User, on_delete=models.CASCADE , related_name= 'workspace_created_by' , null=True)
    members = models.ManyToManyField(User, related_name='members', blank=True, null=True)
    

    def __str__(self):
        return f"{self.name}"
