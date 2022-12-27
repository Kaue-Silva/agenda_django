from django.views.generic import ListView, CreateView
from .models import Agenda
from .forms import AgendaForm
from django.urls import reverse_lazy


class AgendaList(ListView):
    template_name = "agenda_app/list_agenda.html"
    model = Agenda
    

class AgendaCreate(CreateView):
    template_name = "agenda_app/create_agenda.html"
    form_class = AgendaForm
    
    def get_success_url(self):
        return reverse_lazy("agenda_list")
