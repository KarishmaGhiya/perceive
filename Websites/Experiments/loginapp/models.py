from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import logging
# Create your models here.

log = logging.getLogger(__name__)

class Registration(models.Model):
    user = models.ForeignKey(User)
    
    comment = models.CharField(max_length=35, null=True, default=None,blank=True)

    def __str__(self):
        return self.title
