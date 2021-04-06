from django.contrib.auth.models import User 
User.objects.filter(username='adminn').exists() or \
User.objects.create_superuser('adminn', 'admin@admin.com', 'adminnpw')
