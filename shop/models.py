from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Категория", max_length=150, db_index=True)
    slug = models.SlugField("URL", max_length=150, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    name = models.CharField("Название", max_length=200, db_index=True)
    slug = models.SlugField("URL", max_length=200, db_index=True)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    image = models.ImageField("Фото", upload_to='media/products/', blank=True)
    stock = models.PositiveIntegerField("Склад")
    available = models.BooleanField("Активный", default=True)
    created = models.DateTimeField("Дата добавления", auto_now_add=True)
    updated = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])