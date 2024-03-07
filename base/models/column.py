from django.db import models

class Column(models.Model):
    id = models.AutoField(primary_key=True)
    index = models.PositiveIntegerField(null=True)
    title = models.TextField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
