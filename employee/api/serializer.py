from .models import Employee
from rest_framework import serializers

# define the serailizer for the employee model
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def validate_salary_amount(self, salary):
        if salary <= 0:
            raise serializers.ValidationError("Salary most be a  positive value.")
        return salary