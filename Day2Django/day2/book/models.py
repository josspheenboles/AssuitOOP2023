from django.db import models
from author.models import *
# Create your models here.
class Book(models.Model):
    id=models.AutoField(primary_key=True,db_column='ID')
    name=models.CharField(max_length=50)
    authorobj=models.ForeignKey(to='author.Author',on_delete=models.CASCADE)