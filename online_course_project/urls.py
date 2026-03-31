from django.contrib import admin
from django.urls import path
from courses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('submit/<int:course_id>/', views.submit, name='submit'),
    # Corrected to use submission_id to match the view
    path('result/<int:submission_id>/', views.exam_result, name='show_exam_result'),
]