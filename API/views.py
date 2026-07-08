from rest_framework.views import APIView
from rest_framework.response import Response
from .models import create_model,student,employee
from .serializers import create_userSerializers, studentSerializers,employeeSerializers
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView , ListCreateAPIView,RetrieveUpdateDestroyAPIView

class AuthAPIView(APIView):

    # Register
    def post(self, request):
        serializer = create_userSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Account Created Successfully"})

        return Response(serializer.errors)

    # Login
    def put(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = create_model.objects.get(
                email=email,
                password=password
            )

            return Response({"message": "Login Successful"})

        except create_model.DoesNotExist: 
            return Response({"message": "Invalid Email or Password"})
        

class studentList(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=student.objects.all()
    serializer_class=studentSerializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class studentRUD(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=student.objects.all()
    serializer_class=studentSerializers
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


class employeeLC(ListCreateAPIView):
    queryset=employee.objects.all()
    serializer_class=employeeSerializers
class employeeRUD(RetrieveUpdateDestroyAPIView):
    queryset=employee.objects.all()
    serializer_class=employeeSerializers