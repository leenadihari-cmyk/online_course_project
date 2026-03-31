from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Submission, Instructor, Learner

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('text', 'course')

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title',)

class CourseAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('name',)

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('user',)

class LearnerAdmin(admin.ModelAdmin):
    list_display = ('user',)

# Register all models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Learner, LearnerAdmin)