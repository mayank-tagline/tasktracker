from django.db import models
from todo.mixins import CustomIDMixin


class WorkSpace(CustomIDMixin):
    name = models.CharField(max_length=255)
    

    def __str__(self):
        return f"{self.name}"
