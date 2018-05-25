from django.db import models

# Create your models here.
class QuemSomos(models.Model):
    logo = models.ImageField('Logo', upload_to='produto/imagens')
    titulo = models.CharField('Título', max_length=50)
    descricao = models.TextField('Descrição', blank=True, null=True)