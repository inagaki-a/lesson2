from django.db import models

# Create your models here.
class Fruits(models.Model):
    '''
    フルーツモデル
    '''
    id = models.AutoField(verbose_name='id', primary_key=True)
    name = models.CharField(verbose_name='名前', max_length=20)
    memo = models.CharField(verbose_name='メモ', null=True, blank=True, max_length=50)