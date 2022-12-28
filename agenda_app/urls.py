from django.urls import path
from .views import AgendaList, AgendaCreate,  AgendaUpdate

urlpatterns = [
    path("list/", AgendaList.as_view(), name="agenda_list"),
    path("create/", AgendaCreate.as_view(), name="agenda_create"),
    path("update/<int:pk>", AgendaUpdate.as_view(), name="agenda_update")
]
