from django.urls import path
from.views import xyz1,emp_detail,emp_delete,emp_form,emp_update

urlpatterns=[
    path("",xyz1, name="xyz1"),
    path('emp_detail/<int:pk>',emp_detail,name="emp_detail"),
    path('emp_detail/delete/<int:pk>',emp_delete,name="emp_delete"),
    path('emp_detail/create',emp_form,name="emp_form"),
    path('emp_detail/update/<int:pk>',emp_update,name="emp_update")

]