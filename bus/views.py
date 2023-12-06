from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import * 
from .form import * 

def add_bus(request):
    if request.method == "POST":
        form = AddBusForm(request)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Bus added and saved to Database')
            return redirect('all-buses')
        else:
            messages.warning(request, 'Something went wrong. Please check from errors')
            return redirect('add-bus')
    else:
        form = AddBusForm()
        context = {'form':form}
    return render(request, 'bus/add_bus.html', context)

def update_bus(request, pk):
    bus = Bus.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateBusForm(request.POST, instance=bus)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bus information has been updated and saved')
            return redirect('all-buses')
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
    else:
        form = UpdateBusForm(instance=bus)
        context = {'form':form}
    return render(request, 'bus/update_bus.html', context)

def all_buses(request):
    buses = Bus.objects.filter(is_available = True)
    context = {'buses':buses}
    return render(request, 'bus/all_buses.html', context)