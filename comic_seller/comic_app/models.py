from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    comic_pic = models.ImageField(upload_to='pic_folder/', default='pic_folder/no_img.jpg')


    class Meta:
        db_table = 'books'
