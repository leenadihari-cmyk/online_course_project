from django.contrib import admin
from django.urls import path
from courses import views


urlpatterns = [
    path('', views.home, name='home'),  # <-- homepage
    path('admin/', admin.site.urls),
    path('submit/<int:course_id>/', views.submit, name='submit'),
    path('result/<int:submission_id>/', views.show_exam_result, name='show_exam_result'),
]