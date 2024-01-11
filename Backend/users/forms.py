from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input__fields',
                                                             'placeholder':'введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input__fields',
                                                             'placeholder':'введите пароль'}))
    class Meta:
        model = User
        fields = ('username','password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input__fields',
                                                             'placeholder':'Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input__fields',
                                                               'placeholder':'Фамилия'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input__fields',
                                                               'placeholder':'Имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'input__fields',
                                                                 'placeholder':'Электронная почта'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input__fields',
                                                               'placeholder':'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input__fields',
                                                                 'placeholder':'Подтверждение пароля'}))
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs','readonly':True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'inputs' ,'readonly':True}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'profile-image'}),required=False )

    class Meta:
        model = User
        fields = ('first_name','last_name','image','username','email')