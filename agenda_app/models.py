from django.db import models


class Agenda(models.Model):
    compromisso = models.CharField(max_length=255)
    data_hora = models.DateTimeField()
    cliente = models.CharField(max_length=255)
    celular = models.CharField(max_length=11)
    
    class Meta:
        db_table = "agenda"
        
    def __str__(self):
        return f"{self.compromisso} {self.cliente}"