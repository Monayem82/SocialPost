from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class TwieetModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=300)
    photos=models.FileField(upload_to="photos/",blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photos.path) 

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size, Image.Resampling.LANCZOS)
            img.save(self.photos.path)

    def __str__(self):
        return f'{self.user.username} - {self.text}'
