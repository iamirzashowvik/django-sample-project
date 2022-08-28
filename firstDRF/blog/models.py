from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Your user table")
    content = models.TextField(blank=True, null=True, default="My content")
    image = models.FileField(blank=True, null=True, upload_to='media')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Blog Model"
