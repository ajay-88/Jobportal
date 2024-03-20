from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from Myapp.forms import register

# Create your views here.
class Registerview(View):
    def get(self,request,*args,**kwargs):
        form=register()
        return render(request,"Reg.html",{"form":form})
    
    
    def post(self,request,*args,**kwargs):
        form=register(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            
            print(form.cleaned_data)  
        else:
            print("ERROR")

        form=register()
        return render(request,"Reg.html",{"form":form})
    
