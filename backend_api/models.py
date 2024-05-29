from django.db import models


class Material(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    category = models.CharField(max_length=200, verbose_name="Категория")
    code = models.IntegerField(verbose_name="Код материала")
    cost = models.FloatField(verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "materials"