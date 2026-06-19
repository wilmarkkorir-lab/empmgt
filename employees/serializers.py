# department serializer

from rest_framework import serializers

from employees.models import Department, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    # this serializer converts department model data into json format and also allows json data to be converted back into django objects
    # basically acts as the bridge between django model and api response

    class Meta:
        model = Department
        fields = '__all__'
        # include all field from the department model

class EmployeeSerializer(serializers.ModelSerializer):

    # read only meaning shows only full nested department on get request
    department = DepartmentSerializer(read_only=True)

    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source='department',
        write_only=True

    )



    class Meta:
        model = Employee
        fields = '__all__'

        
