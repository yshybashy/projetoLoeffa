from django.db import models

# Create your models here.
class Loefa(models.Model):
  like = models.IntegerField(max_length=1000)
  deslike = models.IntegerField(max_length=1000)
  total = models.IntegerField(max_length=1000)
  gif = models.CharField(max_length=1000)
  active = models.BooleanField(default=True)

  def __str__(self):
    return str(self.id) 

  class Meta:
     db_table = 'loefa'