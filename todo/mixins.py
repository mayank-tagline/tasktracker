import uuid
from datetime import datetime

from django.db import models

MODEL_ALIASES = {
    "User": "usr",
    "WorkSpace": "wrs",
    "Task": "tsk",
}

def generate_custom_id(prefix: str) -> str:
    """Generates a unique custom ID with a prefix."""
    timestamp = datetime.now().strftime("%d%m%y")  # Format: DDMMYY
    short_uuid = uuid.uuid4().hex[:6]  # 6-character UUID
    return f"{prefix}_{timestamp}{short_uuid}"

class CustomIDMixin(models.Model):
    """Mixin to generate a custom unique ID for models."""

    id = models.CharField(
        primary_key=True,
        max_length=50,
        editable=False,
        unique=True,
    )

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        """Automatically assigns a custom ID when an instance is created."""
        super().__init__(*args, **kwargs)
        if not self.id:
            prefix = MODEL_ALIASES.get(
                self.__class__.__name__, self.__class__.__name__[:3].lower()
            )
            self.id = generate_custom_id(prefix)
