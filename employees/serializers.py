from rest_framework import serializers
from employees import constants as employees_constants

class EmployesSerializers(serializers.Serializer):
    # emp_id = serializers.UUIDField(db_index=True)
    # emp_name = serializers.CharField(max_length=30)
    # emp_designation = serializers.CharField(choices=employees_constants.STREAM_CHOICES)
    # emp_datajoing = serializers.DateField()
    # emp_project  = serializers.CharField(max_length=49)
    # emp_id = serializers.UUIDField()
    
    emp_name = serializers.CharField(max_length=30)
    emp_designation = serializers.ChoiceField(choices=employees_constants.STREAM_CHOICES)
    emp_datajoing = serializers.DateField()
    emp_project = serializers.CharField(max_length=49)
    
    
    
class ProjectSerializers(serializers.Serializer):
    pro_name = serializers.CharField(max_length=30)
    pro_designation = serializers.ChoiceField(choices=employees_constants.STREAM_CHOICES)
    pro_datajoing = serializers.DateField()
    pro_project = serializers.CharField(max_length=49)