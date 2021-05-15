from django import forms

attrsFirst = {
    'class': "form-control",
    'style': "margin-bottom: -1px;border-bottom-right-radius: 0;border-bottom-left-radius: 0;"
}

attrsLast = {
    'class': "form-control",
    'style': "margin-bottom: 10px;border-top-left-radius: 0;border-top-right-radius: 0;"
}


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(attrs=attrsFirst)
    )
    password = forms.CharField(
        label='Password',
        max_length=64,
        widget=forms.PasswordInput(attrs=attrsLast)
    )
