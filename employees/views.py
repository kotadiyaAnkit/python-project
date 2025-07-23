import json

from rest_framework.views import APIView
from employees import models as core_models
from employees import utils as core_utils
from employees import serializers as employees_serializers

# Create your views here.
class EmployeeView(APIView):
    def get(self,request):
        employes_get = core_models.EmployeModel.objects.all()
        employe_response = [emp_data.employes_details() for emp_data in employes_get]
        return core_utils.create_response(employe_response,200)
    
    def post(self, request):
        serializers = employees_serializers.EmployesSerializers(data=request.data)
        if not serializers.is_valid():
            return core_utils.create_response(serializers.errors, 400)

        emp_name = serializers.validated_data.get('emp_name')
        emp_designation = serializers.validated_data.get('emp_designation')
        emp_datajoing = serializers.validated_data.get('emp_datajoing')
        emp_project = serializers.validated_data.get('emp_project')
        
        core_models.EmployeModel.objects.create(
            # emp_id =emp_id,
            emp_name=emp_name,
            emp_designation=emp_designation,
            emp_datajoing = emp_datajoing,
            emp_project=emp_project
        )
        
        return core_utils.create_response("Employees Data Saved SuccessFully", 200)
    
class EmployeModifiedViewSet(APIView):
    def get(self, request, emp_id):
        employes_get = core_models.EmployeModel.objects.filter(emp_id=emp_id).last()
        
        if not employes_get:
            return core_utils.create_response("Employe 's Data Not Found", 400)
        
        return core_utils.create_response(employes_get.employes_details(), 200)
    
    def put(self, request, emp_id):
        serializers = employees_serializers.EmployesSerializers(data=request.data)
        
        if not serializers.is_valid():
            return employees_serializers.create_response(serializers.errors, 400)
        
        employes_get = core_models.EmployeModel.objects.filter(emp_id=emp_id).last()
        
        if not employes_get:
            return core_utils.create_response("Employees Data not Found", 400)
        
       
        employes_get.emp_name =  serializers.validated_data.get('emp_name')
        employes_get.emp_designation = serializers.validated_data.get('emp_designation')
        employes_get.emp_datajoing = serializers.validated_data.get('emp_datajoing')
        employes_get.emp_project = serializers.validated_data.get('emp_project')
        
        employes_get.save()
        return core_utils.create_response(employes_get.employes_details(), 200)
    
    def delete(self, request, emp_id):
        employes_get = core_models.EmployeModel.objects.filter(emp_id=emp_id).last()
        
        if not employes_get:
            return core_utils.create_response("Emplyee Data Not Found", 400)
        
        employes_get.delete()
        return core_utils.create_response("Employee Data Deleted successfully",200)
    
# get->      id used serach the data ex = localhost/employess/1 
# class EmployeModifiedViewSet(APIView):
#     def get(self, request, enroll_id):
#         try:
#             employee = core_models.EmployeModel.objects.get(id=enroll_id)
#             employee_data = employee.employes_details()  
#             return core_utils.create_response(employee_data, 200)
#         except core_models.EmployeModel.DoesNotExist:
#             return core_utils.create_response({"error": "Employee not found"}, 404)


# Create your views here.
class ProjectView(APIView):
    def get(self,request):
        proj_get = core_models.Project.objects.all()
        proj_response = [emp_data.employes_details() for emp_data in proj_get]
        return core_utils.create_response(proj_response,200)
    
    def post(self, request):
        serializers = employees_serializers.ProjectSerializers(data=request.data)
        if not serializers.is_valid():
            return core_utils.create_response(serializers.errors, 400)

        emp_name = serializers.validated_data.get('emp_name')
        emp_designation = serializers.validated_data.get('emp_designation')
        emp_datajoing = serializers.validated_data.get('emp_datajoing')
        emp_project = serializers.validated_data.get('emp_project')
        
        core_models.Project.objects.create(
            # emp_id =emp_id,
            emp_name=emp_name,
            emp_designation=emp_designation,
            emp_datajoing = emp_datajoing,
            emp_project=emp_project
        )
        
        return core_utils.create_response("Employees Data Saved SuccessFully", 200)
    