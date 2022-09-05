from django.contrib import admin
from models.UserProfiles import UserProfile
from models.Followers import Followers

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Followers)