from django.db import models

# Create your models here.
class Records(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    company_name= models.CharField(max_length=50)
    date_of_registration= models.CharField(max_length=50)
    company_registration_number=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    contact_person=models.CharField(max_length=50)
    list_of_departments=models.CharField(max_length=50)
    number_of_emlpoyees=models.CharField(max_length=50)
    contact_phone=models.CharField(max_length=50)
    email_address=models.CharField(max_length=50)
    name_of_employee=models.CharField(max_length=50)
    employee_id=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    date_started=models.CharField(max_length=50)
    date_left_role=models.CharField(max_length=50)
    duties=models.CharField(max_length=50)


    def __str__(self):
        return(f"{self.company_name} {self.email_address}")
    
