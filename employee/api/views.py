from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework import viewsets, permissions, status

# Create your views here.
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=['patch'], url_path='update-promotion-points')
    def update_promotion_points(self, request, pk=None):
        employee = self.get_object()
        points = request.data.get('promotion_points', None)
        if points is not None:
            employee.promotion_points = points
            employee.save()
            return Response({'status': 'Promotion points updated'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)