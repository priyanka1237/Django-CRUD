from django.db import models
class Department(models.Model):
    dept_name=models.CharField(max_length=50)
    def __str__(self):
        return self.dept_name

class Employee(models.Model):
    department= models.ForeignKey(Department, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    designation=models.CharField(max_length=60)
    objects=models.Manager()
    def __str__(self):
        return self.first_name