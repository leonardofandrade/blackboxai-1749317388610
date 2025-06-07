from django.contrib.auth.models import User
from django.core.management import setup_environ
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doctor_office_management.settings')
django.setup()

user = User.objects.get(username='admin')
user.set_password('admin123')
user.save()
print("Password updated successfully!")
