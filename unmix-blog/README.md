---

## unmix-blog:

"unmix-blog" uses 2 containers and 3 tools. One container has this app, alpine and gunicorn and one container has nginx and alpine.

You can only deploy this app with "docker-compose".

Run "docker-compose up -d --build" (unmix-blog/docker-compose.yml)

Default super user name is 'admin'.

Default super user password is 'adminpw'.

*Run "docker-compose down -v --rmi" to remove all containers, networks, volumes and images.

---

## You have to do for settings.py:

unmix-blog/django_project/settings.py

### Change 4 lines(# Change to yours) for "Reset password" function:

*The email setting is for "Gmail". You may need different setup for other emails.

```
##### Email setting for "Reset password" function #####

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' # Change to yours
EMAIL_PORT = 587 # Change to yours
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'example@gmail.com' # Change to yours
EMAIL_HOST_PASSWORD = 'abcdefg' # Change to yours

########################################################
```

---

## Optional for settings.py:

unmix-blog/django_project/settings.py

===

### Change "SECRET_KEY" for more security:

```
SECRET_KEY = 'abcdefg' # Change to yours
```

===

### There is the setting for postgresql:

If you use postgresql rather than default sqlite, comment out the sqlite setting and uncomment the postgresql setting then change 4 lines(# Change to yours).

*You need to install and configure postgresql yourself.

```
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_sqlite3',
    }
}
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb', # Change to yours
        'USER': 'myuser', # Change to yours
        'PASSWORD': 'mypw', # Change to yours
        'HOST': '10.156.58.93', # Change to yours
        'PORT': '5432',
    }
}
```

===

### There is the setting for aws s3 bucket:

If you use aws s3 bucket rather than default app file system, uncomment the aws s3 bucket setting then change 3 lines(# Change to yours).

```
##### AWS s3 bucket setting #####

AWS_ACCESS_KEY_ID = 'example' # Change to yours
AWS_SECRET_ACCESS_KEY = 'example' # Change to yours
AWS_STORAGE_BUCKET_NAME = 'example-bucket' # Change to yours
 
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

STATICFILES_STORAGE = 'django_project.s3utils.StaticRootS3Boto3Storage'
DEFAULT_FILE_STORAGE = 'django_project.s3utils.MediaRootS3Boto3Storage'

##################################
```

*I commented out the code in "unmix-blog/users/models.py" to enable this app to work with "AWS s3 bucket" properly.

Otherwise, this app doesn't work with "AWS s3 bucket" properly.

```
'''
    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
'''
```

===

### If you use gmail, do 2 things below to get over very strong google's security.

1. Allow less secure apps: ON ---> https://myaccount.google.com/lesssecureapps

2. Allow access to your Google account: ON (Tap "Continue") ---> https://accounts.google.com/DisplayUnlockCaptcha

===

---

## Snippet for docker-compose deployment:

===

### Just run "docker-compose up -d --build":

unmix-blog/docker-compose.yml, unmix-blog/Dockerfile

There are "docker-compose.yml" and "Dockerfile".

*Run "docker-compose down -v --rmi" to remove all containers, volumes and images.

===

### Change createsuperuser.py (Optional):

unmix-blog/createsuperuser.py

1. Change two 'admin' for your super user name:
2. Change an 'admin@admin.com' for your email address:
3. Change an 'adminpw' for your super user password:

```
User.objects.filter(username='admin').exists() or \
User.objects.create_superuser('admin', 'admin@admin.com', 'adminpw')
```

*It works properly with default setting so you don't need to change it if you don't want.

===

---
