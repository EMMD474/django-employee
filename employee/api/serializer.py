from .models import Employee
from rest_framework import serializers

# define the serailizer for the employee model
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
