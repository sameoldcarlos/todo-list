from django.db import models
from uuid import uuid4

# Create your models here.

class Task(models.Model):

    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done')
    )
    id_task = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)
    status = models.CharField(
        max_length=5,
        choices = STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title