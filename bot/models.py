from django.db import models
from django.utils.text import slugify
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class BotUser(models.Model):
    user_id = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    phoneNumber = models.CharField(max_length=200, null=True)
    was_online = models.DateTimeField(default=timezone.now) # it means time_since_last_activity time or Time since last message
    recent_reaction_time = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.username

    def get_message_count(self):
        # Retrieve the count of messages sent by this BotUser
        return self.bot.aggregate(message_count=Count('id'))['message_count']
    
    def time_since_last_reaction(self):
        # Check if recent_reaction_time is not set
        if self.recent_reaction_time is None:
            return "N/A"  # or any other default value
        
        # Calculate the time difference
        time_difference = timezone.now() - self.recent_reaction_time
        
        # Check if the time difference is less than a minute
        if time_difference.total_seconds() < 60:
            # Convert time difference to seconds
            seconds_difference = int(time_difference.total_seconds())
            return f"{seconds_difference} seconds"
        # Check if the time difference is less than an hour
        elif time_difference.total_seconds() < 3600:
            # Convert time difference to minutes
            minutes_difference = int(time_difference.total_seconds() / 60)
            return f"{minutes_difference} minutes"
        # Check if the time difference is less than a day
        elif time_difference.total_seconds() < 86400:
            # Convert time difference to hours
            hours_difference = int(time_difference.total_seconds() / 3600)
            return f"{hours_difference} hours"
        else:
            # Convert time difference to days
            days_difference = time_difference.days
            return f"{days_difference} days"
        
        
        
    def time_since_last_message(self):
        # Get the last message sent by this BotUser
        last_message = self.bot.filter(bot_user=self).latest('time')
        
        # Calculate the time difference
        time_difference = timezone.now() - last_message.time
        
        # return time_difference.days
        # Check if the time difference is less than a minute
        if time_difference.total_seconds() < 60:
            # Convert time difference to seconds
            seconds_difference = time_difference.total_seconds()
            return f"{int(seconds_difference)} seconds"
        # Check if the time difference is less than an hour
        elif time_difference.total_seconds() < 3600:
            # Convert time difference to minutes
            minutes_difference = time_difference.total_seconds() / 60
            return f"{int(minutes_difference)} minutes"
        # Check if the time difference is less than a day
        elif time_difference.total_seconds() < 86400:
            # Convert time difference to hours
            hours_difference = time_difference.total_seconds() / 3600
            return f"{int(hours_difference)} hours"
        else:
            # Convert time difference to days
            days_difference = time_difference.days
            return f"{days_difference} days"
    
# 
    
class MessageContent(models.Model):
    message_id = models.CharField( max_length=200, unique=True)
    bot_user = models.ForeignKey(BotUser,on_delete=models.CASCADE, related_name='bot')
    message_content = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    react_emoji = models.CharField(max_length=200, null=True)
    react_count = models.CharField(max_length=200,  null=True)
    
    

    
    

