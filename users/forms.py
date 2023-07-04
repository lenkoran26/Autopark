from django.contrib.auth.models import User

from django import forms


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        help_texts = {
            'username': 'Только буквы, цифры и символы @/./+/-/_',
        }
        
        error_messages = {
            'username': {
                'required': 'Это поле обязательно для заполнения',
                 },
            
            'password': {
                'required': 'Это поле обязательно для заполнения',
            },
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password2']