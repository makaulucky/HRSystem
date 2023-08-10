from django.contrib import admin
from . models import Company, Department, Employee

# Register your models here.


admin.site.register(Company)

admin.site.register(Department)
admin.site.register(Employee)

admin.site.site_header = "HR Admin System"
admin.site.site_title = "System Admin"
admin.site.index_title = "Welcome to HRM"