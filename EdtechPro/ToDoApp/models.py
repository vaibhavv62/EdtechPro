from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=32)

    def __str__(self):
        return self.category_name

class Task(models.Model):
    category = models.ForeignKey(Category,default="General",on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    details = models.CharField(max_length=512,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    due_date_time = models.DateTimeField()

    class Meta:
        ordering = ["-created"]  # ordering by the created field
