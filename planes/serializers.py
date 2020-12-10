from rest_framework import serializers
from .models import Plan

class Planserielizers (serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = ["NombrePlan","descripcion","precio","fecha"]
