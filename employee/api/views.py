from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework import viewsets, permissions, status

# Create your views here.
# view for the employee model
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.AllowAny]

    # custom endpoint to update promoetion points
    @action(detail=True, methods=['patch'], url_path='update_promotion')
    def update_promotion_points(self, request, pk=None):
        employee = self.get_object()
        points = request.data.get('promotion_points', None)

        # check if the promotion_points have been provided
        if points is not None:
            if int(points) >= 0:
                employee.promotion_points = points
                employee.save()
                return Response({'status': 'Promotion points updated'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'Promotion points cannot be below 0'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)