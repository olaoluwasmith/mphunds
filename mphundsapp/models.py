from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4

User = get_user_model()

def f():
    d = uuid4()
    str = d.hex
    return str[0:13]

# Create your models here.
