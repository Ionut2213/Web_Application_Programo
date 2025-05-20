from django.shortcuts import render, redirect


from .models import Feedback
from .forms import FeedbackForm
# Create your views here

def add_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.save()
            return redirect('list-feedback')
    
    else:
        form = FeedbackForm()
    return render(request, 'feedback/add_feedback.html', {'form' : form})



def list_feedback(request):
    feedback = Feedback.objects.all()
    return render(request, 'feedback/list_feedbacks.html', {'feedbacks': feedback})



def history_feedback(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback/history_feedback.html', {'feedbacks': feedbacks})
