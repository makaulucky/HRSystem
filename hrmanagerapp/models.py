from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField('Comapny',max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Department(models.Model):
    name = models.CharField('Department',max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class Employee(models.Model):
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    email = models.EmailField()
    gender = models.CharField(max_length=100, choices=GENDER)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.TextField()
    # insurance = models.CharField(max_length=100)
    nssf_number = models.CharField('NSSF Number',max_length=100)
    nhif_number = models.CharField('NHIF Number',max_length=100)
    kra_pin = models.CharField('KRA PIN',max_length=100)
    # Next of kin data
    nextofkin_first_name = models.CharField('Next of Kin First Name',max_length=100)
    nextofkin_middle_name = models.CharField('Next of Kin Middle Name',max_length=100, blank=True, null=True)
    nextofkin_last_name = models.CharField('Next of Kin(s) Last Name',max_length=100)
    nextofkin_country = models.CharField('Next of Kin(s) Country',max_length=100)
    nextofkin_city = models.CharField('Next of Kin(s) City',max_length=100)
    nextofkin_address = models.CharField('Next of Kin Address',max_length=100)
    nextofkin_phone = models.CharField('Next of Kin(s) Phone',max_length=100)
    nextofkin_email = models.EmailField('Next of Kin(s) Email',max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
    class META:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
    