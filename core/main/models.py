from django.db import models

class Category(models.Model):
    name = models.CharField('Category name', max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Phone(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='catphone', null=True)
    name = models.CharField('Phone name', max_length=30)
    about = models.TextField('Phone about')
    price = models.IntegerField('phone price')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'
        