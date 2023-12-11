from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from transport.models import Route

@login_required
def dashboard(request):
    routes = Route.objects.all()
    context = {
        'routes':routes
    }
    return render(request, 'dashboard/dashboard.html', context)