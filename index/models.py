from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title_en = models.CharField(max_length=256, null=True, blank=True)
    title_ru = models.CharField(max_length=256, null=True, blank=True)
    img = models.FileField(upload_to='country/')



class Product(BaseModel):
    title_en = models.CharField(max_length=256, null=True, blank=True)
    title_ru = models.CharField(max_length=256, null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.FileField(upload_to='product/')
    price = models.CharField(max_length=56, null=True, blank=True, default=0)
