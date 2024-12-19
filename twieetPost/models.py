from django.db import models
from django.contrib.auth.models import User

class TwieetModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=300)
    photos=models.FileField(upload_to="photos/",blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text}'
