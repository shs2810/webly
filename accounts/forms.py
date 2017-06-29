from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyUser

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'required': 'True',
        }
    ))
    lastname = forms.RegexField(label="Lastname", max_length=30,
                                regex=r'^[\w.@+-]+$',
                                help_text="이름을 입력하시오.",
                                error_messages={
                                    'invalid': "This value may contain only letters, numbers and "
                                               "@/./+/-/_ characters."},
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Lastname',
                                    'required': 'true',
                                }))

    firstname = forms.RegexField(label="Firstname", max_length=30,
                                regex=r'^[\w.@+-]+$',
                                help_text="성을 입력하시오.",
                                error_messages={
                                    'invalid': "This value may contain only letters, numbers and "
                                               "@/./+/-/_ characters."},
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Firsttname',
                                    'required': 'true',
                                }))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password confirmation',
                'required': 'True',
            }
        ),
        help_text="Enter the same password as above, for verification."
    )

    class Meta:  # SignupForm에 대한 기술서
        model = MyUser
        fields = ("email", "lastname", "firstname", "sex",)  # 작성한 필드만큼 화면에 보여짐

class LoginForm(AuthenticationForm):
    email = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'nickname',
                'required': 'True',
            }
        )
    )
    lastname = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'lastname',
                'required': 'True',
            }
        )
    )
    firstname = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'firstname',
                'required': 'True',
            }
        )
    )
    sex = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'sex',
                'required': 'True',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )