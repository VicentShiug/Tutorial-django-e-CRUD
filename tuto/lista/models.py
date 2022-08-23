from pydoc import describe
from django.db import models

class ToDo(models.Model):
    
    STATUS = (
        ('A fazer', 'A fazer'),
        ('Feito', 'Feito'),
    )
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.CharField(
        max_length= 7, choices=STATUS, blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'ToDo'

    def __str__ (self):
        return self.titulo