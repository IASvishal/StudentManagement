from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created =True)
    name = models.CharField(max_length=50)
    roll_number = models.IntegerField(unique=True)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    photo = models.ImageField(
        upload_to="students/",
        blank=True,
        null=True
    )

    def __name__(self):
        return self.name