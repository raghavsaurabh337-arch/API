from django.contrib import admin
# from .models import login_model
from .models import create_model,student,employee,school_library

# # Register your models here.
admin.site.register(create_model)
admin.site.register(student)


class create_user(admin.ModelAdmin):
     list_display=['email','password','Repassword']

class student(admin.ModelAdmin):
     list_display=['name','age','course','father_name']
class employee(admin.ModelAdmin):
     list_display=['name','salary','villege','Department']
