# from django.db import models

import uuid
from django.db import models
from employees import constants as employees_constants

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


class Project(BaseModel):
    pro_name = models.CharField(max_length=100)
    pro_start_date = models.DateField()
    pro_client_name = models.CharField(max_length=100)
    pro_designation = models.CharField(max_length=25,choices=employees_constants.PROJECT_CHOICES, default="Developer")

    def __str__(self):
        return self.pro_name  # Changed from self.name

    def Project_details(self):
        return {
            "pro_name": self.pro_name,
            "pro_start_date": self.pro_start_date,
            "pro_client_name": self.pro_client_name,
            "pro_desifnation" : self.pro_designation
        }


class EmployeModel(BaseModel):
    emp_id = models.UUIDField(default=uuid.uuid4, db_index=True)
    emp_name = models.CharField(max_length=100)
    emp_designation = models.CharField(max_length=25,choices=employees_constants.STREAM_CHOICES)
    emp_datajoing = models.DateField()

    emp_project = models.ForeignKey(Project, on_delete=models.CASCADE)  # Linked by ForeignKey

    emp_project  = models.CharField(max_length=49)


    def employes_details(self):
        emp_data = {
            "emp_id" : self.emp_id,
            "emp_name" : self.emp_name,
            "emp_designation" : self.emp_designation,
            "emp_datajoing" : self.emp_datajoing,
            "emp_project" : self.emp_project
        }

        return emp_data

        return emp_data

