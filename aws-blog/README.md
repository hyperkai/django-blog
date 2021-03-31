--- 

## aws-blog:

"aws-blog" has an app with aws s3 bucket setting on settings.py. Then, it's run with "python manage.py 0.0.0.0:8000".

Moreover, you can use 2 deployment methods,"manual deployment" and "docker-compolse deployment".
"docker-compolse deployment" is recommanded because you don't need to manually deploy the app 
running "python3 -m venv venv", "source venv/bin/activate", pip install -r requirements.txt" and so on.

---

## You have to do for settings.py for 2 deployments:
aws-blog / django_project / settings.py

===

### Change to yours:

SECRET_KEY = 'abcdefg' (Line 11) <-- If you don't mind security, don't need to change 'abcdefg' which works properly.

AWS_ACCESS_KEY_ID = 'example' (Line 107)

AWS_SECRET_ACCESS_KEY = 'example' (Line 108)

AWS_STORAGE_BUCKET_NAME = 'example-bucket' (Line 109)

===

### Change to yours for "Reset Password" function:

EMAIL_HOST = 'smtp.gmail.com' (Line 128)

EMAIL_PORT = 587 (Line 129)

EMAIL_HOST_USER = 'example@gmail.com' (Line 131)

EMAIL_HOST_PASSWORD = 'abcdefg' (Line 132)

===

---

## Optional:

### If you use gmail, do 2 things below to get over very strong google's security.

1. Allow less secure apps: ON ---> https://myaccount.google.com/lesssecureapps

2. Allow access to your Google account: ON (Tap "Continue") ---> https://accounts.google.com/DisplayUnlockCaptcha

---

## Snippet for manual deployment:

The version "Python 3.8.5" is recommended to use but the above versions will be fine.

"python manage.py collectstaic" is already run. So don't run "python manage.py collectstaic" otherwise error occurs.

You may need to run "pip install wheel" before running "pip install -r requirements.txt". Otherwise, error will occur.

After running "pip install -r requirements.txt""pip install -r requirements.txt", run "python manage.py migrate".

Then, create a super user running "python manage.py createsuperuser".

Finally, run "python manage.py runserver 0.0.0.0:8000".

---

## Snippet for docker-compose deployment:

===

### Change createsuperuser.py (Optional):
aws-blog / createsuperuser.py

1. Change two 'admin' for your super user name:
2. Change 'admin@admin.com' for your email address:
3. Change 'adminpw' for your super user password:

User.objects.filter(username='admin').exists() or \
User.objects.create_superuser('admin', 'admin@admin.com', 'adminpw')

*It works properly with default setting so you don't need to change it if you don't want.

===

There's already been "docker-compose.yml" and "dockerfiles" in this folder.

So just run "docker-compose up -d --build" for deployment.

Then run "docker-compose down -v --rmi" to remove all containers, volumes and images.

---
