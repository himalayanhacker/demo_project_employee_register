from django.urls import path
from myempapp import views
urlpatterns = [
    path('',views.index),
    path('login/',views.loginuser,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('employee/',views.employee_form,name='emp_insert'),
    path('<int:id>/',views.employee_form,name='upd'),
    path('list/',views.employee_list,name='emp_list'),
    path('del<int:id>/',views.employee_delete, name='emp_del'),
    path('signup/',views.sign_up, name='signup'),
    path('changepass/',views.user_change_pass, name='changepass'),
]