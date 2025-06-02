from rest_framework import serializers
from .models import Plan    
from .models import GymInfo


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"

class GymInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymInfo
        fields = "__all__"