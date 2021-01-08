from django.db import models


# Create your models here.
class Users(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    login_id = models.CharField(max_length=36, null=False)
    login_pw = models.CharField(max_length=36, null=False)

    class Meta:
        ordering = ['created', 'modified']

