from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = "Enter Username"
        self.fields['password1'].widget.attrs['placeholder'] = "Enter Password"
        self.fields['password2'].widget.attrs['placeholder'] = "Confirm Password"
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


class UserUpdateForm(UserChangeForm):
    password = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = "Change User Name"
        self.fields['username'].help_text = ''

        self.fields['email'].widget.attrs['placeholder'] = "Change Email"
        self.fields['email'].help_text = ''

        self.fields['first_name'].widget.attrs['placeholder'] = "Change First Name"
        self.fields['first_name'].help_text = ''

        self.fields['last_name'].widget.attrs['placeholder'] = "Change Last Name"
        self.fields['last_name'].help_text = ''


class UserPassChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class UserPhotoUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


