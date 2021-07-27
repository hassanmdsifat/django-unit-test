from django.db import models


class ModelA(models.Model):
    name = models.CharField(max_length=200)
    name_two = models.CharField(max_length=200)

    class Meta:
        db_table = 'model_a'


class ModelB(models.Model):
    name = models.CharField(max_length=200)
    name_two = models.CharField(max_length=200)

    class Meta:
        db_table = 'model_b'