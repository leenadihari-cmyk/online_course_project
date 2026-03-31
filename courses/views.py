from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Question, Choice, Submission
from django.contrib.auth.decorators import login_required

# Home page view
def home(request):
    courses = Course.objects.all()
    return render(request, 'courses/home.html', {'courses': courses})

# Exam page view
@login_required
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    questions = course.question_set.all()

    if request.method == 'POST':
        total_score = 0
        for q in questions:
            selected_choice_id = request.POST.get(str(q.id))
            if selected_choice_id:
                choice = Choice.objects.get(id=int(selected_choice_id))
                if choice.is_correct:
                    total_score += 1

        # Save submission
        submission = Submission.objects.create(
            user=request.user,
            course=course,
            score=total_score
        )
        # Redirect to the exam result page using submission.id
        return redirect('show_exam_result', submission_id=submission.id)

    return render(request, 'courses/submit.html', {'course': course, 'questions': questions})

# Exam result view
@login_required
def exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    course = submission.course
    return render(request, 'courses/exam_result.html', {'course': course, 'submission': submission})