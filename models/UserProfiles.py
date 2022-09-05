from django.db import models

class UserProfile(models.Model):

    class Meta:
        app_label = "accounts"

    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
