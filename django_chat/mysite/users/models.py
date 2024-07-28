from django.db import models
from django.contrib.auth.models import User

def user_director_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_director_path, default="placeholder.png")
    is_online = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username