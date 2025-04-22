import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devsearch.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin12345'
        )
        print("Superuser created: admin/admin12345")
    else:
        print("Superuser already exists")

if __name__ == "__main__":
    create_superuser()
