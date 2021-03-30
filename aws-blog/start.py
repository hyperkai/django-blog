from django.contrib.auth.models import User 
#if User.objects.filter(username='kai').exists():
#    print("try")
#else:
#    print("else")
#try:
#    if User.objects.filter(username='kai').exists():
#        print("try")
#except OperationalError as error:
#        print("except")    
User.objects.filter(username='kai').exists() or \
User.objects.create_superuser('kai', 'kazya.ito.dream@gmail.com', 'dream')