import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UniqueUserEmailField(forms.EmailField):

    def validate(self, value):
        super(forms.EmailField, self).validate(value)
        try:
            User.objects.get(email=value)
            raise forms.ValidationError("Email already exists")
        except User.MultipleObjectsReturned:
            raise forms.ValidationError("Email already exists")
        except User.DoesNotExist:
            pass


class ExtendedUserCreationForm(UserCreationForm):

    username = forms.CharField(required=True, max_length=30)
    email = UniqueUserEmailField(required=True, label='Email address')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['email',
                                'password1', 'password2']

    def clean(self, *args, **kwargs):
        cleaned_data = super(UserCreationForm, self).clean(*args, **kwargs)
        return cleaned_data

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit)
        if user:
            user.email = self.cleaned_data['email']
            user.set_password(self.cleaned_data['password1'])
            if commit:
                user.save()
        return user
        
        
        
        