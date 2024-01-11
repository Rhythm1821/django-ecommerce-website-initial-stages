from django.db import models
from uuid import uuid4

class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,editable=False,default=uuid4)
    created_up=models.DateTimeField(auto_now_add=True)
    updated_up=models.DateTimeField(auto_add=True)

    class Meta:
        abstract=True