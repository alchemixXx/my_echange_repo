from django.db import models

class Users(models.Model):
    user_first_name = models.CharField(max_length=264)
    user_last_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264, unique=True)

    def __str__(self):
        return self.email




# class Record(models.Model):
#     adress = models.ForeignKey(Email, null=True, on_delete=models.SET_NULL)
#     date = models.DateField()






# Create your models here.
