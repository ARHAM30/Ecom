from django.db import models
from Ecom.utils import unique_slug_generator
from django.db.models.signals import pre_save
from PIL import Image
# Create your models here.



class Category(models.Model):
    title     =models.CharField(max_length=120)
    sub_title =models.CharField(max_length=120,blank=True,null=True)
    image     =models.ImageField(upload_to='category_img')
    slug      =models.CharField(max_length=120,blank=True,null=True)


    def __str__(self):
        return str(self.title)

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 420 or  img.width > 260:
            output_size = (420, 260)
            img.thumbnail(output_size)
            img.save(self.image.path)


def catagorysignal(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(catagorysignal,sender=Category)


class Products(models.Model):
    title           =models.CharField(max_length=120)
    description     =models.TextField(max_length=1200)
    image           =models.ImageField(upload_to="product_image")
    category        =models.ForeignKey(Category,on_delete=models.CASCADE)
    real_price      =models.IntegerField(null=True, blank=True)
    dicount_price   =models.IntegerField()
    slug = models.SlugField(max_length=100, blank=True, null=True)
    publish     =models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)


def prodsignal(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(prodsignal,sender=Products)


