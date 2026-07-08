from .models import create_model,student,employee,school_library
from rest_framework import serializers

class create_userSerializers(serializers.ModelSerializer):
     class Meta:
          model = create_model
          fields = '__all__'
class studentSerializers(serializers.ModelSerializer):
     class Meta:
          model = student
          fields = '__all__'
class employeeSerializers(serializers.ModelSerializer):
     class Meta:
          model = employee
          fields = '__all__'
class school_librarySerializers(serializers.ModelSerializer):
     class Meta:
          model = school_library
          fields = '__all__'
