import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from api.models.user_models import User

# Create superuser
if not User.objects.filter(email='admin123@gmail.com').exists():
    user = User.objects.create_superuser(
        email='admin123@gmail.com',
        password='admin123'
    )
    print(f"Superuser created: {user.email}")
else:
    print("Superuser already exists")