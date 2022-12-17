from django.db import models

# Create your models here.

# each type, helps us for these following:
#    - make django choose suitable html widget for this type
#    - validation
#    - db size
choices = [
     ("part-time", "part-time"),
     ("full-time", "full-time")
]
class Job(models.Model): # models.Model === Table
     title = models.CharField(max_length=100) # === column
     type = models.CharField(max_length=15, choices=choices)
     salary = models.IntegerField(default=0);
     vacancy = models.IntegerField(default=1)
     description = models.TextField(max_length=1000);
     category = models.ForeignKey("Category", models.CASCADE, default=1)

     def __str__(self) -> str:
          return self.title;

class Category(models.Model):
     name = models.CharField(max_length=20);

     def __str__(self) -> str:
          return self.name;