from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'email',
            'name': 'email',
            'class': 'form-control'
            }
        ),
        required=True)
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'password',
                'name': 'password',
                'class': 'form-control',
                'type': 'password'
                }
            ),
        required=True)


class RegisterForm(forms.Form):
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'firstname',
            'name': 'firstname',
            'class': 'form-control'
            }
        ),
        required=True)
    lastname = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'lastname',
            'name': 'lastname',
            'class': 'form-control'
            }
        ),
        required=True)
    email = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'email',
            'name': 'email',
            'class': 'form-control'
            }
        ),
        required=True)
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'password',
                'name': 'password',
                'class': 'form-control',
                'type': 'password'
                }
            ),
        required=True)
    confirm_password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'confirm_password',
                'name': 'confirm_password',
                'class': 'form-control',
                'type': 'password'
                }
            ),
        required=True)
