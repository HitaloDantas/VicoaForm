from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
from people.models import Person, Ponto
from datetime import datetime


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('nome', 'cpf', 'nascimento', 'login_crm', 'senha_crm','id_fast', 'permissao', 'skill', 'empresa', 'status', 'telefone1', 'telefone2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))


class PontoForm(forms.ModelForm):
    usuario = forms.CharField(initial=User.username)

    class Meta:
        model = Ponto
        fields = ('usuario',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))











