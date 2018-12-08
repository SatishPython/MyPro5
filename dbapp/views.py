from django.shortcuts import render
from . models import Product

def Input(request):
    return render(request, 'input.html')
def Insert(request):
    Pid=int(request.GET['t1'])
    Pname=request.GET['t2']
    Pcost=float(request.GET['t3'])
    Pmfdt=request.GET['t4']
    Pexpdt=request.GET['t5']

    f=Product(Pid=Pid,Pname=Pname,Pcost=Pcost,Pmfdt=Pmfdt,Pexpdt=Pexpdt)
    f.save()
    return render(request,'links.html')

def Display(request):
    recs=Product.objects.all()
    return render(request,'display.html',{'records':recs})



# Create your views here.
