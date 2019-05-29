from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', required=True)
    password = forms.CharField(label='密码', required=True, min_length=6)
