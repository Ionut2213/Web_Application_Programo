from django import forms
from pacienti.models import Pacient


class PacientiForm(forms.ModelForm):
    class Meta:
        model = Pacient
        fields = '__all__'


        widgets = {
            'first_name' : forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            
            'last_name' : forms.TextInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Please enter your last name'}),

            'email' : forms.EmailInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Please enter your email addresss'}),

            'phone' : forms.TextInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Please enter your phone number'}),

            'gender' : forms.Select(
                attrs={'class': 'form-control', 'placeholder' : 'Select gender'}),
            
            'location' : forms.Select(
                attrs={'class' : 'form-control', 'placeholder' : 'Select location'}),

            'start_date' : forms.DateInput(
                attrs={'class' : 'form-control', 'type': 'date', 'placeholder' : 'Select start date'}
            )
        }
    
    def clean(self):
        cleaned_data = super(PacientiForm, self).clean()

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        check_name = Pacient.objects.filter(first_name=first_name, last_name=last_name)
        if check_name:
            msg = 'Pacient with the name already exists.'
            self.add_error('first_name', msg)


class PacientUpdateForm(forms.ModelForm):
    class Meta:
        model= Pacient
        fields = '__all__'

        widgets = {
            'first_name' : forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            
            'last_name' : forms.TextInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Please enter your last name'}),

            'email' : forms.EmailInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Please enter your email addresss'}),

            'phone' : forms.TextInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Please enter your phone number'}),

            'gender' : forms.Select(
                attrs={'class': 'form-control', 'placeholder' : 'Select gender'}),
            
            'location' : forms.Select(
                attrs={'class' : 'form-control', 'placeholder' : 'Select location'}),

            'start_date' : forms.DateInput(
                attrs={'class' : 'form-control', 'type': 'date', 'placeholder' : 'Select start date'}
            )
        }
