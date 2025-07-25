from rest_framework import serializers
from employees import constants as employees_constants
from employees.models import EmployeModel, Project


class EmployesSerializers(serializers.ModelSerializer):
    emp_project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = EmployeModel
        fields = ['emp_name', 'emp_designation', 'emp_datajoing', 'emp_project']
# class EmployesSerializers(serializers.Serializer):
#     emp_name = serializers.CharField(max_length=30)
#     emp_designation = serializers.ChoiceField(choices=employees_constants.STREAM_CHOICES)
#     emp_datajoing = serializers.DateField()
#     emp_project = serializers.CharField(max_length=49)
    
    

    
    
    
class ProjectSerializers(serializers.Serializer):
    pro_name = serializers.CharField(max_length=30)
    pro_start_date = serializers.DateField()
    pro_client_name = serializers.CharField()
    pro_designation =serializers.ChoiceField(choices=employees_constants.PROJECT_CHOICES)

  

