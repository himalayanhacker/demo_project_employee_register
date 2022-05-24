from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myempapp.models import Employee
class MyEmployeeform(forms.ModelForm):
    class Meta:
        model= Employee
        fields='__all__'
        labels= {
            'fullname':'Full Name',
            'emp_code':'EMP. Code',
        }
class Signupfrom(UserCreationForm):
    password2=forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields=['username','first_name','last_name','email']
        labels={
            'email':"Email",
        }

# class Changepasswordform(PasswordChangeForm):
#     class Meta:
#         model= User
#         fields=['old_password','new_password1','new_password2']
        # def __init__(self,*args,**kargs):
        #     super(MyEmployeeform,self).__init__(*args,**kargs)
        #     self.fields['position'].empty_label='Select'
        #     self.fields['emp_code'].required = False