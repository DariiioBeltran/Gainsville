from django.db import models

class Followers(models.Model):

    class Meta:
        app_label = "accounts"
        unique_together = ['user_id', 'following_user_id']

    user_id = models.ForeignKey("UserProfile", related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey("UserProfile", related_name="followers", on_delete=models.CASCADE)