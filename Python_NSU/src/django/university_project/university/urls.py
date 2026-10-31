from django.urls import path
from . import views

urlpatterns = [
    # Университеты
    path('universities/', views.university_list,
         name='university_list'),
    path('universities/create/', views.university_create,
         name='university_create'),
    path('universities/<int:pk>/edit/', views.university_update,
         name='university_update'),
    path('universities/<int:pk>/delete/', views.university_delete,
         name='university_delete'),

    # Студенты
    path('students/', views.student_list,
         name='student_list'),
    path('students/create/', views.student_create,
         name='student_create'),
    path('students/<int:pk>/edit/', views.student_update,
         name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete,
         name='student_delete'),
]