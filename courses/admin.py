from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Submission, Instructor, Learner

# Inline models for admin
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

# Admin configurations
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('text', 'course')

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title',)

class CourseAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('name',)

# Register models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Instructor)
admin.site.register(Learner)