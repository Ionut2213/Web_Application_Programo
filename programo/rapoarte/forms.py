from django import forms

class ReportForm(forms.Form):
    report_choice = [
        ('pacienti', 'Pacienti'),
        ('notite', 'Notite'),
        ('feedback', 'Feedback'),
    ]


    select_choice = [
        ('select_all', 'Selecteaza Tot'),
        ('select_by_name', 'Selecteaza dupa nume'),
    ]

    report_type = forms.ChoiceField(choices=report_choice, label="Tip Raport")
    selection_criteria = forms.ChoiceField(choices=select_choice, label = "Criteriu de selectie")
    name = forms.CharField(required=False, label = "Nume", max_length=100)
    start_date = forms.DateField(required=False, label="Data de inceput", widget=forms.SelectDateWidget)
    end_date = forms.DateField(required=False, label="Data de sfarsit", widget=forms.SelectDateWidget)
