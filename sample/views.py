from django.shortcuts import render,redirect
from .models import order
from .forms import orderForm
# Create your views here.
def home(request):
    data=order.objects.all()
    return render(request,'home.html',{'data':data})
def create_order(request):
    form=orderForm()
    if request.method=='POST':
        form=orderForm(request.POST)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'order_form.html',context)

def update_order(request,pk):
    orders=order.objects.get(id=pk)
    form=orderForm(instance=orders)
    if request.method=='POST':
        form=orderForm(request.POST,instance=orders)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'update_form.html',context)

def delete_order(request,pk):
    orders=order.objects.get(id=pk)
    if request.method=='POST':
        orders.delete()
        return redirect('home')
    context={'item':orders}
    return render(request,'delete.html',context)