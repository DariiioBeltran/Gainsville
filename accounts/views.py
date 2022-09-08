from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from models.UserProfiles import UserProfile

# Create your views here.

class LoginPage(TemplateView):
    template_name = "login_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            users = UserProfile.objects.all()
        )

        return context