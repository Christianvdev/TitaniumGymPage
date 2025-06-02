from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Plan
from .models import GymInfo

from .serializers import PlanSerializer
from .serializers import GymInfoSerializer


# Create your views here.
def PlanList(request):
    plans = Plan.objects.all()
    plansSerializer = PlanSerializer(plans, many=True)

    gymdata = GymInfo.objects.first()
    gymDataSerializer = GymInfoSerializer(gymdata)

    varDict = {
        'plans': plansSerializer.data,
        'gymInfo' : gymDataSerializer.data
    }

    return render(request, 'plans.html', varDict)

def homeView(request):
    plans = Plan.objects.all()
    plansSerializer = PlanSerializer(plans, many=True)

    gymdata = GymInfo.objects.first()
    gymDataSerializer = GymInfoSerializer(gymdata)

    #List all variables we need to access
    varDict = {
        'plans': plansSerializer.data,
        'gymHome' : gymDataSerializer.data,
    }


    #render the page
    return render(request, 'home.html', varDict)
