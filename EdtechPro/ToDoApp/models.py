from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=32)

    def __str__(self):
        return self.category_name

class Task(models.Model):
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=512)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    category = models.ForeignKey(Category,default="General",on_delete=models.CASCADE)
