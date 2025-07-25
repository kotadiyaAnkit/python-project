from django.urls import path
from employees import views




urlpatterns = [
     path('', views.EmployeeView.as_view(), name='employees'),
     path('project/', views.ProjectView.as_view(), name='project'),
    path('employees/<uuid:emp_id>/', views.EmployeModifiedViewSet.as_view(), name="data_updation"),

    # path('employees/<uuid:emp_id>/', views.EmployeModifiedViewSet.as_view(), name="data_updation"),

]