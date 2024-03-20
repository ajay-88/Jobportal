from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    categoryname=models.CharField(max_length=20,unique=True)


    def __str__(self):
        return self.categoryname
    

class Job(models.Model):
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    salary = models.PositiveIntegerField()
    qualification = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    poster=models.ImageField(upload_to="poster")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Student(models.Model):
    # name=models.CharField(max_length=200)
    age=models.PositiveIntegerField()
    qualification=models.CharField(max_length=200)
    skill=models.CharField(max_length=200)
    contact=models.CharField(max_length=30)
    resume=models.FileField(upload_to="files",null=True)
    experience=models.CharField(max_length=200)
    options=(
        ("male","male"),("female","female"),("others","others")
    )
    gender=models.CharField(max_length=20,choices=options,default="male")
    user=models.OneToOneField(User,on_delete=models.DO_NOTHING,null=True,related_name="profile")


    def __str__(self):
        return self.name


class Applications(models.Model):
    jobs=models.ForeignKey(Job,on_delete=models.CASCADE)
    student=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    options=(
        ("pending","pending"),("rejected","rejected"),("processing","processing")
        )
    status=models.CharField(max_length=30,choices=options,default="pending")
    