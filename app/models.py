from django.db import models

# Create your models here.

class Department(models.Model):
    dept_name=models.CharField(max_length=100)
    dept_no=models.IntegerField(primary_key=True)
    loc=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.dept_name




class Employee(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_no=models.IntegerField()
    dept_no=models.ForeignKey(Department,on_delete=models.CASCADE)
    emp_job=models.CharField(max_length=100)
    emp_sal=models.IntegerField()

    def __str__(self) -> str:
        return self.emp_name