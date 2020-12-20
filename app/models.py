from django.db import models
from datetime import date
import re

# Create your models here.
class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        
        today = date.today()
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        
        
        if postData['fname']=='' :
            errors['fname']= "You have to have a first name!"
        if postData['lname']=='':
            errors['lname']= "Please enter a last name!"
        if postData['email']=='':
            errors['email']= "Please enter an email"
        elif not EMAIL_REGEX.match(postData['email']):   
            errors['email'] = "Invalid email address!"
        elif len(User.objects.filter(email=postData['email']))>0:
            errors['email'] = "Email already register. Try signing in."
        if postData['pw']=='':
            errors['pw']="You need to have a password!"
        elif postData['pw']!=postData['cpw']:
            errors['pw']="Passwords don't match!"
        return errors   
    
    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        user= User.objects.filter(email=postData['email'])
        if len(user)== 0:
            errors['email'] = "Can't find user with that email. Try signing up."
        elif postData['pw']!=user[0].password:
            errors['invalid']= 'Invalid login Information'
        return errors
    
    def update_validator(self, postData, user):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if postData['fname']=='' :
            errors['fname']= "You have to have a first name!"
        if postData['lname']=='':
            errors['lname']= "Please enter a last name!"
        if postData['email']=='':
            errors['email']= "Please enter an email"
        elif not EMAIL_REGEX.match(postData['email']):   
            errors['email'] = "Invalid email address!"
        elif postData['email']!=user.email:
            if len(User.objects.filter(email=postData['email']))>0:
                errors['email'] = "Email already register to another account"
        return errors
    def quote_validator(self, postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['author'])<3 :
            errors['author']= "Author name must have more than 3 characters!"
        if len(postData['quote'])<10:
            errors['quote']= "Qoute must be at least 10 character!"
        return errors
        
class User(models.Model):
    first_name= models.CharField(max_length=45)
    last_name= models.CharField(max_length=45)
    email= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= UserManager()
    def __str__(self):
        return f"<User object: {self.first_name} ({self.id})>"
    
class Quote(models.Model):
    author= models.CharField(max_length=45)
    quote= models.CharField(max_length=255)
    user= models.ForeignKey(User, related_name="quotes", on_delete= models.CASCADE)
    likes = models.ManyToManyField(User, related_name = "liked_quotes", default={})
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)