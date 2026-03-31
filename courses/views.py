from django.shortcuts import render, get_object_or_404
from .models import Course, Question, Choice, Submission
from django.contrib.auth.decorators import login_required


def home(request):
    courses = Course.objects.all()
    return render(request, 'courses/home.html', {'courses': courses})
@login_required
def submit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    score = 0
    if request.method == "POST":
        for question in course.question_set.all():
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                choice = Choice.objects.get(id=selected_choice_id)
                if choice.is_correct:
                    score += 1
        Submission.objects.create(user=request.user, course=course, score=score)
    return render(request, 'courses/submit.html', {'course': course, 'score': score})

@login_required
def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    return render(request, 'courses/exam_result.html', {'submission': submission})