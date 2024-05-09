from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    # name_ar = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    view = models.ImageField(upload_to='item_view', blank=True, null=True)
    view2 = models.ImageField(upload_to='item_view2', blank=True, null=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    # category_ar = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    # name_ar = models.CharField(max_length=255)
    # description_ar = models.TextField(blank=True, null=True)
    # price_ar = models.FloatField()
    # view_ar = models.ImageField(upload_to='item_view', blank=True, null=True)
    # view2_ar = models.ImageField(upload_to='item_view2', blank=True, null=True)
    # image = models.ImageField(upload_to='item_images', blank=True, null=True)
    # is_sold_ar = models.BooleanField(default=False)
    # created_by_ar = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    # created_at_ar = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name