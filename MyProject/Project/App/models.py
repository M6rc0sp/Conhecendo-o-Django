from django.db import models

# Create your models here.
class QuemSomos(models.Model):
    logo = models.ImageField('Logo', upload_to='produto/imagens', blank=True)
    titulo = models.CharField('Título', max_length=50)
    descricao = models.TextField('Descrição', blank=True, null=True)
    class Meta:
        verbose_name = "Quem somos"
    def __str__(self):
        return self.titulo