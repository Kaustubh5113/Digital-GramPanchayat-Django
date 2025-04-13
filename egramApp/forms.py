from django import forms
from .models import User
from django.contrib.auth.models import User
from .models import Transaction
from .models import HomeTax
from django.utils import timezone

# class EventForm(forms.ModelForm):
    # class Meta:
    #     model = Event
    #     fields = ['title', 'short_description', 'details']
    #     widgets = {
    #         'title': forms.TextInput(attrs={
    #             'class': 'form-control', 
    #             'placeholder': 'Enter Event Title', 
    #             'style': 'border-radius: 5px; padding: 10px; font-size: 14px;'
    #         }),
 

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['user_name', 'amount', 'status', 'last_date']
        
class ScreenshotUploadForm(forms.ModelForm):
    class Meta:
        model = HomeTax
        fields = ['screenshot']
        
# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['title', 'short_description', 'details']

class UploadScreenshotForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['screenshot', 'upload_date']
    
    # Ensures upload_date is set to today's date by default
    upload_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), initial=timezone.now)
