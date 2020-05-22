from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from people.models import Person, Usuario, Ponto
from people.forms import PersonForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Count
from .models import Usuario


class PontoCreateView(CreateView):
    model = Ponto
    fields = ('usuario',)
    template_name = 'people/ponto.html'
    context_object_name = 'people'
    success_url = reverse_lazy('ponto')


class PersonListView(ListView):
    model = Person
    template_name = 'templates/person_list.html'
    context_object_name = 'people'


class PersonCreateView(CreateView):
    login_required = True
    model = Person
    fields = ('nome', 'cpf', 'nascimento', 'login_crm', 'senha_crm', 'id_fast', 'permissao', 'skill', 'empresa', 'status', 'telefone1', 'telefone2')
    success_url = reverse_lazy('person_list')


class PersonUpdateView(UpdateView):
    login_required = True
    model = Person
    form_class = PersonForm
    template_name = 'people/person_update_form.html'
    success_url = reverse_lazy('person_list')

@login_required
def pie_chart(request):
    labels = []
    data = []

    queryset = Usuario.objects.values('permissao').annotate(total=Count('permissao'))
    for entry in queryset:
        labels.append(entry['permissao'])
        data.append(entry['total'])

    return render(request, 'people/pie_chart.html', {
        'labels': labels,
        'data': data,
    })












