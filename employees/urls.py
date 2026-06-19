from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employees.views import EmployeeDetailView, EmployeeListView, DepartmentViewSet

router = DefaultRouter()
router.register('departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('employees/', EmployeeListView.as_view()),
    path('employees/<int:pk>/', EmployeeDetailView.as_view()),
]
