from djongo import models
from bson import ObjectId

class ObjectIdField(models.Field):
    def get_prep_value(self, value):
        if not value:
            return ObjectId()
        if not isinstance(value, ObjectId):
            return ObjectId(value)
        return value

class User(models.Model):
    id = ObjectIdField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    # ...other fields...

class Team(models.Model):
    id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)
    # ...other fields...

class Activity(models.Model):
    id = ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    # ...other fields...

class Leaderboard(models.Model):
    id = ObjectIdField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()
    # ...other fields...

class Workout(models.Model):
    id = ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.IntegerField()
    # ...other fields...