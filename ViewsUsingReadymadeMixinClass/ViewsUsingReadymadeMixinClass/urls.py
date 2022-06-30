
from django.contrib import admin
from django.urls import path
from student import views
'''
Method 1 Urls:
---------------
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentsapi/',views.StudentList.as_view()),
    path('poststudentapi/',views.StudentCreate.as_view()),
    path('studentapi/<int:pk>/',views.StudentRetrieve.as_view()),
    path('putstudentapi/<int:pk>/',views.StudentUpdate.as_view()),
    path('delstudentapi/<int:pk>/',views.StudentDestroy.as_view()),
]
'''
'''
# Method 2 URL pattern:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.LCStudentAPI.as_view()),
    path('studentapi/<int:pk>/',views.RUDStudentAPI.as_view()),
]
'''

# Method 3 URL pattern:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.StudentListCreate.as_view()),
    path('studentapi/<int:pk>/',views.StudentRetrieveUpdateDestroy.as_view()),
]