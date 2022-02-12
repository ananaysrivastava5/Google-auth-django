from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.http import HttpResponse
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import render


class MySocialAccount(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        u = sociallogin.user
        if u.email.split('@')[1] not in  ["squadstack.com", "squadiq.in", "squadrun.com"]:
            raise ImmediateHttpResponse(render(request, 'account/error.html'))
        