from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("students/", views.StudentListView.as_view()),
    path("students/<int:pk>/", views.StudentDetailView.as_view()),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
    path("teachers/", views.TeacherListView.as_view()),
    path("teachers/<int:pk>/", views.TeacherDetailView.as_view()),
]
urlpatterns += format_suffix_patterns(urlpatterns)