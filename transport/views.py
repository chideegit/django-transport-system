from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import * 
from .models import *
from bus.models import Bus

def add_route(request):
    if request.method == 'POST':
        form = AddRouteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New routed added and saved in the Database')
            return redirect('add-route')
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
            return redirect('add-route')
    else:
        form = AddRouteForm()
        context = {'form':form}
    return render(request, 'transport/add_route.html', context)

def update_route(request, pk):
    route = Route.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateRouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            messages.success(request, 'Route information updated and saved to the Database')
            return redirect('all-routes')
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
    else:
        form = UpdateRouteForm(instance=route)
        context = {'form':form}
    return render(request, 'transport/update_route.html', context)

def all_routes(request):
    routes = Route.objects.all()
    context = {'routes':routes}
    return render(request, 'transport/all_routes.html', context)

def buses_in_route(request, pk):
    route = Route.objects.get(pk=pk)
    get_route=route.bus_set.all()
    context = {'route':get_route, 'r':route}
    return render(request, 'transport/buses_in_route.html', context)