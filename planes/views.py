from django.http import request
from django.shortcuts import render, get_object_or_404
from .models import Plan
from django.utils import timezone

# Create your views here.

def plan_list(request):
    planes = Plan.objects.all()
    return render(request, 'planes/plan_list.html', {'planes': planes})

def plan_venta(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    return render(request, 'planes/plan_venta.html', {'plan' : plan}) 