from django.contrib import admin
# from .models import login_model
from .models import create_model,student,employee,school_library

# # Register your models here.
admin.site.register(create_model)
admin.site.register(student)
admin.site.register(employee)
admin.site.register(school_library)


class create_user(admin.ModelAdmin):
     list_display=['email','password','Repassword']

class student(admin.ModelAdmin):
     list_display=['name','age','course','father_name']
class employee(admin.ModelAdmin):
     list_display=['name','salary','villege','Department']
class school_library(admin.ModelAdmin):
     list_displya=['name','course','book_no','bookName','address']     

 