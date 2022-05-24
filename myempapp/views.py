from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login,update_session_auth_hash
from myempapp.forms import MyEmployeeform,Signupfrom
from django.contrib.auth.forms import PasswordChangeForm
from myempapp.models import Employee
from django.contrib import messages
# Create your views here.
def employee_list(request):
    sh=Employee.objects.all()
    return render(request,"employee_list.html",{'sh':sh})


def employee_form(request,id=0):
    if request.user.is_authenticated:
        if request.method=='POST':
            if id==0:
                form = MyEmployeeform(request.POST)
            else:
                emp=Employee.objects.get(pk=id)
                form=MyEmployeeform(request.POST,instance=emp) 
                
            if form.is_valid():
                form.save()
                messages.success(request, 'Your data is submited')
                return redirect('/list')         
        else:
            if id==0:
                form=MyEmployeeform()
            else:
                emp=Employee.objects.get(pk=id)
                form = MyEmployeeform(instance=emp)
        
        return render(request,"employee_form.html",{'form':form})
    else:
        return HttpResponseRedirect('/login/')


def employee_delete(request,id):
    Employee.objects.get(pk=id).delete()
    messages.success(request, 'Your data is deleted')
    return redirect('/list')



def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request,'login.html')



def loginuser(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
            # A backend authenticated the credentials
                login(request,user)
                return redirect('/employee')
            else:
            # No backend authenticated the credentials
                return render(request,'login.html')

        return render(request,'login.html')
    return HttpResponseRedirect('/employee/')


    
def logoutuser(request):
    logout(request)
    return redirect('/login')


def sign_up(request):
        if request.method=='POST':
            frm= Signupfrom(request.POST)
            if frm.is_valid():
                frm.save()
            messages.success(request,'Account Created Successfully ! ')
            return HttpResponseRedirect('/signup/')
        else:
            frm= Signupfrom()
        return render(request,'signup.html',{'form':frm})


def user_change_pass(request):
    if request.user.is_authenticated:
            if request.method=='POST':
                frm= PasswordChangeForm(user=request.user,data=request.POST)
                if frm.is_valid():
                    frm.save()
                    update_session_auth_hash(request,frm.user)
                    messages.success(request,'Password Changed Successfully !')
                    return HttpResponseRedirect('/employee/')
            else:
                frm= PasswordChangeForm (user=request.user)
            return render(request,'changepass.html',{'form':frm}) 
    else:
        return HttpResponseRedirect('/login/')