from django.contrib.auth.models import User 
User.objects.filter(username='admin').exists() or \
User.objects.create_superuser('admin', 'admin@admin.com', 'adminpw')
