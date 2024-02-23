from .models import Job_detail,Applicant
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

        
class AddJobs(ModelForm):
    job_dateline = forms.DateField(widget=forms.SelectDateWidget(years=range(2024,2030)),required=False)
    class Meta:
        model = Job_detail
        fields='__all__'
        
class SignupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class JSignupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['name','email','website','cv','cover_letter']
        
class EmployerStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['applicant_status']

