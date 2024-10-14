from django.urls import path, include
from api.views import EmployeeViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'employee', EmployeeViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls'))
]