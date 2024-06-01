from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Material(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='materials', verbose_name='Категория')
    code = models.IntegerField(verbose_name="Код материала")
    cost = models.FloatField(verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "materials"


class Category(MPTTModel):
    title = models.CharField(max_length=200, unique=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        db_table = "category"
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('material-by-category', args=[int(self.id)])

    def __str__(self):
        return self.title
