# from django.db import models

import uuid
from django.db import models
from employees import constants as employees_constants

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

class Project(BaseModel):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    client_name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class EmployeModel(BaseModel):
    emp_id = models.UUIDField(default=uuid.uuid4, db_index=True)
    emp_name = models.CharField(max_length=100)
    emp_designation = models.CharField(max_length=25,choices=employees_constants.STREAM_CHOICES)
    emp_datajoing = models.DateField()
    emp_project = models.ForeignKey(Project, on_delete=models.CASCADE)  # Linked by ForeignKey

    def employes_details(self):
        emp_data = {
            "emp_id" : self.emp_id,
            "emp_name" : self.emp_name,
            "emp_designation" : self.emp_designation,
            "emp_datajoing" : self.emp_datajoing,
            "emp_project" : self.emp_project
        }
        return emp_data