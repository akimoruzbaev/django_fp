from django import forms

inputAttrs = {
    'class': "form-control"
}


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(attrs=inputAttrs)
    )
    password = forms.CharField(
        label='Password',
        max_length=64,
        widget=forms.PasswordInput(attrs=inputAttrs)
    )


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs=inputAttrs))
    password = forms.CharField(widget=forms.PasswordInput(attrs=inputAttrs))
    firstName = forms.CharField(widget=forms.TextInput(attrs=inputAttrs))
    lastName = forms.CharField(widget=forms.TextInput(attrs=inputAttrs))
    email = forms.CharField(widget=forms.EmailInput(attrs=inputAttrs))


class CommentForms(forms.Form):
    # text = forms.Textarea()
    text = forms.CharField(widget=forms.Textarea(attrs=inputAttrs))


class NewPostForm(forms.Form):
    title = forms.CharField(max_length=250, widget=forms.TextInput(attrs=inputAttrs))
    clipped_text = forms.CharField(max_length=150, widget=forms.Textarea(attrs=inputAttrs))
    text = forms.CharField(widget=forms.Textarea(attrs=inputAttrs))
