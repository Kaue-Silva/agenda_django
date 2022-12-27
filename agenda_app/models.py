from django.db import models


class Agenda(models.Model):
    compromisso = models.CharField(max_length=255)
    data_hora = models.DateTimeField()
    cliente = models.CharField(max_length=255)
    
    class Meta:
        db_table = "agenda"