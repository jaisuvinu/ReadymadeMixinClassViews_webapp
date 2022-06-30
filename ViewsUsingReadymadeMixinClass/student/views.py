from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin

from student.models import Student
from student.serializer import StudentSerializer

'''
Method:1 (creating seperate classes for every CRUD operations)
---------

class StudentList (GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request,*args, **kwargs)

class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self,request, *args,**kwargs):
        return self.create(request,*args,**kwargs)


class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class StudentDestroy(GenericAPIView,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs)
'''

'''
# Method 2:(creating two classes and list the relevant mixins in it and create relevant funtions)

# List and Create primary key(pk) not required
class LCStudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
# Get by id ,Update and Delete requires id
class RUDStudentAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
'''

'''
#Advanced Method:
#Method 3:(create only Two API classes without funtions )
----------

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
'''


#Method 4:(creating RestAPIs using ViewSet Class )
#---------






