from __future__ import unicode_literals
from django.db import models

import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex = re.compile(r'^[a-zA-Z]+$')


class UserManager(models.Manager):

    def register_validate(self, postData):
        errors = {}
        a = User.objects.filter(email = postData['email'])
        
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First name must be at least 2 characters."
        elif not name_regex.match(postData['first_name']):
            errors["first_name"] = "First name must contain only letters."

        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name must be at least 2 characters."
        elif not name_regex.match(postData['last_name']):
            errors["last_name"] = "Last name must contain only letters."

        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid e-mail address."
        elif a:
            errors["email"] = "The email already exists in our system. Please type another one."

        if len(postData['password']) < 1:
            errors["password"] = "Please enter your password."
        elif len(postData['password']) < 5:
            errors["password"] = "Password must be more than 4 characters long."
        
        if len(postData["password_con"]) < 1:
            errors["password_con"] = "Please verify your password."
        elif postData["password_con"] != postData['password']:
            errors["password_con"] = "The passwords do not match."
        return errors
    
    def login_validate(self, postData):
        user = User.objects.filter(email = postData['email'])
        errors = {}

        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid e-mail address."
        if len(postData['password']) < 1:
            errors["password"] = "Please enter your password."
        elif len(user) == 0:
            errors["password"] = "Cannot find e-mail address in our system. Please register."
        elif not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
            errors["password"] = "Incorrect password. Please try again."

        return errors
    
    def success(self):
        message = {}
        message['register'] = "You have successfully registered!"
        message['login'] = "You have successfully logged in!"

        return message


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()