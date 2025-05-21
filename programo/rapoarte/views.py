from django.shortcuts import render, get_object_or_404

from .forms import ReportForm
from .models import Report
from pacienti.models import Pacient
from notes.models import Note
from feedback.models import Feedback
from django.http import HttpResponse

# Create your views here.


def generate_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report_type = form.cleaned_data['report_type']
            selection_criteria = form.cleaned_data['selection_criteria']
            name = form.cleaned_data['name']
            start_date = form.changed_data['start_date']
            end_date = form.changed_data['end_date']


            if report_type == 'pacienti':
                if selection_criteria == 'select_all':
                    records = Pacient.objects.filter(created_at_range = [start_date, end_date])
                else:
                    records = Pacient.objects.filter(nume_icontains = name, created_at_range = [start_date, end_date])
                
                if not records.exists():
                    return HttpResponse("Nu exita inregistrati pentru criteria selectata")
                

                # Raport pentru pacienti

                content = "Rapoarte Pacienti\n\n"
                for pacient in records:
                    content += f"Nume: {pacient.nume}\n"
                content += "\n"

        elif report_type == 'notite':
            if selection_criteria == 'select_all':
                records = Note.objects.filter(created_at_range = [start_date, end_date])
            else:
                records = Note.objects.filter(title_icontains = name, created_at_range = [start_date, end_date])

                if not records.exists():
                    return HttpResponse("Nu exista inregistrari pentru criteria selectata")
                

                # Rapoarte pentru notite

                content = "Rapoarte Notite\n\n"
                for notite in records:
                    content += f"Titlu: {notite.title}\n"
                    content += f"Continut: {notite.content}\n"

                content += "\n"



        elif report_type == 'feedback':
            if selection_criteria == 'select_all':
                records = Feedback.objects.filter(session_date_range = [start_date, end_date])
            else:
                record = Feedback.objects.filter(message_icontains = name,
                                                 session_date_range = [start_date, end_date])

            if not records.exists():
                return HttpResponse("Nu exista inregistrari pentru criteria selectata")

            content = "Rapoarte Feedback: \n\n"
            for feedback in records:
                content += f"Pacient: {feedback.pacient}\n"
                content += f"Data Sesiunii: {feedback.session_date}\n"
                content += F"Mesaj: {feedback.message}\n"
            content += "\n"
        return HttpResponse(content)
    else:
        form = ReportForm()
    return render(request, 'rapoarte/generate_report.html', {'form' : form})
