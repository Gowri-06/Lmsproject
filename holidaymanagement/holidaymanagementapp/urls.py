from django.urls import path
from .views import *

urlpatterns = [
    # path('members/', views.members, name='members'),
    path("",holidayaddform,name="holidayaddform"),
    path("form_data_save/",form_data_save,name="form_data_save"),
    path("viewpage/",viewpage,name="viewpage"),
    path("viewpageone/<int:id>/",viewpageone,name="viewpageone"),
    path("update/<int:id>/",update,name="update"),    
    path("updaterecord/<int:id>/",updaterecord,name="updaterecord"),
    path("delete/<int:id>/",delete,name="delete"),






]