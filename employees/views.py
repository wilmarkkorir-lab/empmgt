from django.shortcuts import render
from rest_framework import viewsets,generics

from employees.models import Department, Employee
from employees.serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.
#  departments view sets

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer


# generic views will handle the employee//handles the get and the posts request
class EmployeeListView(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

# get one/put/delete
class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

   
