from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

# Create your views here.

@login_required
def note_list(request):
    notes = Note.objects.filter(user = request.user)
    return render(request, 'notes/note_list.html', {'notes' : notes})



@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    return render(request, 'notes/note_detail.html', {'note' : note})



@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            form.save_m2m()
            return redirect('note_list')
        
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form' : form})


@login_required
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})



@login_required
def note_archive(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    note.archive()
    return redirect('note_list')
