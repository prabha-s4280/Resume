from django.shortcuts import render
def resume_view(request):
    context={
        'first_name':'Sunnam','last_name':'Prabhas','address':'GKRM','mail':'prabhasunnam1@gmail.com','ph_no':7993382441
    }
    return render(request,'index.html',context)