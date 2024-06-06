from django.urls import path
from .import views

urlpatterns = [
   
   path('', views.home, name='home'),
   path('course', views.course, name='course'),
   path('dashboard', views.dashboard, name='dashboard'),
   path('profile', views.profile, name='profile'),
   path('message', views.message, name='message'),
   path('register', views.register, name='register'),
   path('login', views.user_login, name='login'),
   path('logout', views.user_logout, name='logout'),
   path('course', views.service, name='course'),
   path('about', views.about, name='about'),
   path('student', views.student, name='student'),
   path('sign_up', views.form, name='sign_up'),
   path('submit', views.SignUP, name='submit'),
   path('send', views.send, name='send'),
   path('search', views.search_courses, name='search'),
   path('editAbout/<int:id>',views.editAbout, name='editAbout'),
   path('admin_course', views.adminCourse, name='admin_course'),
   path("edit_custom_user/<int:id>", views.edit_custom_user, name='edit_custom_user'),
   path('delete_custom_user/<int:id>', views.delete_custom_user, name='delete_custom_user'),
   path('delete_message/<int:id>', views.delete_message,name='delete_message'),
   path('view_message/<int:id>',views.view_message, name='view_message'),
   path('view_student_record/<int:id>', views.view_student_record, name='view_student_record'),
   path("edit_student_record/<int:id>", views.edit_student_record, name='edit_student_record'),
   path('delete_student_record/<int:id>', views.delete_student_record, name='delete_student_record'),
   path('edit_about/<int:id>', views.edit_about, name='edit_about'),
   path('edit_course/<int:id>/', views.edit_course, name='edit_course'),
   path('delete_admin_course/<int:id>', views.delete_course, name='delete_admin_course'),
   path('insert_course', views.insert_course, name='insert_course'),
]
