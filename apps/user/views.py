from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.core.urlresolvers import reverse

# Create your views here.
from user.forms import LoginForm


class UserLoginApi(View):
    def get(self, request):
        return render(request, template_name='login.html', context={})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, template_name='login.html', context={})
            else:
                return render(request, template_name='login.html', context={})
        return render(request, template_name='login.html', context={})
