from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Pacient
from .forms import PacientiForm, PacientUpdateForm

# Create your views here.

class PacientCreateView(LoginRequiredMixin, CreateView):
    template_name = 'pacienti/create_pacient.html'
    model = Pacient
    form_class = PacientiForm
    success_url = reverse_lazy('client-page')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()
        context['pacients'] = Pacient.objects.all()
        return context
    

    def form_valid(self, form):
        new_pacient = form.save(commit=False)
        new_pacient.first_name = new_pacient.first_name.title()
        new_pacient.last_name = new_pacient.last_name.title()

        new_pacient.save()
        subject = 'Add new Pacient'

        details = {
            'full_name' : f'{new_pacient.first_name} {new_pacient.last_name}',
        }
        return super(PacientCreateView, self).form_valid(form)


  
class PacientListView(LoginRequiredMixin, ListView):
    template_name = 'pacienti/list_of_pacienti.html'
    model = Pacient
    context_object_name = 'all_pacients'


    def get_queryset(self):
        return Pacient.objects.all()
    

class PacientUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'pacienti/update_pacienti.html'
    model = Pacient
    form_class = PacientUpdateForm
    success_url = reverse_lazy('list-pacients')


class PacientDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'pacienti/delete_pacienti.html'
    model = Pacient
    success_url = reverse_lazy('list-pacients')


@login_required()
def delete_pacient(request, pk):
    pacient = get_object_or_404(Pacient, pk=pk)
    if request.method == 'POST':
        pacient.delete()
        return redirect('list-pacients')
    
    return render(request, 'pacienti/delete_pacienti.html', {'pacient' : pacient})