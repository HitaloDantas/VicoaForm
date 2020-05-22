from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.contrib import admin
from people.views import PersonListView, PersonCreateView, PersonUpdateView, pie_chart, PontoCreateView
from people import views



urlpatterns = [
    #path('', views.pie_chart, name='pie-chart'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('list', login_required(PersonListView.as_view()), name='person_list'),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
    path('add/', login_required(PersonCreateView.as_view()), name='person_add'),
    path('', login_required(PontoCreateView.as_view()), name='ponto'),
    path('<int:pk>/edit/', login_required(PersonUpdateView.as_view()), name='person_edit'),

]