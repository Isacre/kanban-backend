from django.db import models

class Card(models.Model):
    column = models.ForeignKey('base.Column', on_delete=models.DO_NOTHING)
    index = models.PositiveIntegerField()
    title = models.TextField(max_length=255)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)