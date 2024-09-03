from django.db import models

# Create your models here.


class User(models.Model):
    uid= models.AutoField(primary_key=True)
    name= models.CharField(max_length=500)
    email= models.CharField(max_length=500)
    address= models.CharField(max_length=500)
    phoneno= models.CharField(max_length=500)
    password= models.CharField(max_length=500)
    
    class Meta :
        db_table = 'user'


class Dept(models.Model):
    d_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500) 
    u_id = models.IntegerField(default=0)
    active_id =  models.IntegerField(default=0)
 
    class Meta :
        db_table = 'dept'


class Addvisitor(models.Model):
    vid= models.AutoField(primary_key=True )
    fullname= models.CharField(max_length=500)
    emailid= models.CharField(max_length=500)
    phoneno= models.CharField(max_length=10)
    address= models.CharField(max_length=500)
    companyname= models.CharField(max_length=500)
    whometomeet= models.CharField(max_length=500)
    department= models.CharField(max_length=500)
    reasontomeet= models.CharField(max_length=500)
    wheretomeet= models.CharField(max_length=500)
    datetomeet= models.CharField(max_length=500)
    timetomeet= models.CharField(max_length=500)
    uid = models.IntegerField(default=0) 
    active_id = models.IntegerField(default=0) 

    class Meta :
        db_table = 'addvisitor'



                             


 
