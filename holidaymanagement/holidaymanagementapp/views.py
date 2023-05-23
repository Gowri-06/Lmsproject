from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import *
from django.urls import reverse
from django.template import loader
# from datetime import datetime
from datetime import datetime



# def index(request):
#     return HttpResponse('hello world')

# Create your views here.
def holidayaddform(request):
    return render(request,'holidayaddform.html')

def form_data_save(request):
    print("inside form_data_save function")
    if request.method == "POST":
        type_holiday = request.POST.get("selected_option1")
        created_at = request.POST.get("from_date")
        name = request.POST.get("name")
        country = request.POST.get("selected_option2")
        print( type_holiday,created_at, name, country)
        store_data = LmsPublic(type_holiday=type_holiday, created_at=created_at,name=name,country=country)
        store_data.save()
        print("store_data",store_data)
        return HttpResponseRedirect(reverse('holidayaddform'))
    else:
        return render(request, "holidayaddform.html")
    
def viewpage(request):
    data = LmsPublic.objects.all().values().order_by('-created_at')
    print(data)
    l = []
    for i in data:
        print(i)
        date_only = i["created_at"]
        date_value = date_only.date()
        print(date_only)
        
        i["created_at"] = date_value 
        # l.append(i)
        my_object =LmsPublic(**i) 
        my_object.save()
        print("my_object",(my_object))
    data = LmsPublic.objects.all().values().order_by('-created_at')

    template = loader.get_template('viewholiday.html')
    context = {
        "data":data,
        
      

    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("db_data")

def viewpageone(request,id):
    data = LmsPublic.objects.get(id=id)
    print(data)
    template = loader.get_template('singleholiday.html')
    context = {
        "data":data,
    }
    return HttpResponse(template.render(context, request))

def update(request,id):
    get_data = LmsPublic.objects.get(id=id)
    print("get_data",get_data) 
    template = loader.get_template('update.html')
    context = {
        "data":get_data
    }
    return HttpResponse(template.render(context, request))     

def updaterecord(request,id):
    update_data = LmsPublic.objects.get(id=id)
    print(update_data)
    type_holiday = request.POST.get("selected_option1")
    created_at = request.POST.get("from_date")
    name = request.POST.get("name")
    country = request.POST.get("selected_option2")
    # update_student_data = Student.objects.filter(id=id)

    # update_student_data(name=name,age=age)
    update_data.name = type_holiday
    update_data.age = created_at 
    update_data.roll_no = name    
    update_data.roll_no = country    
    update_data.save()
    # update_data = Student.objects.get(id=id)
    # print("upfdddddddddddd",update_data.name)
    return HttpResponseRedirect(reverse('viewpage'))

    # return HttpResponse("db_data")
def delete(request,id):
    delete_data =  LmsPublic.objects.get(id=id)
    print(delete_data)
    delete_data.delete()
    return HttpResponseRedirect(reverse('viewpage'))