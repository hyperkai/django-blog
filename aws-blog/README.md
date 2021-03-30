--- 

## aws-blog:

"aws-blog" has an app with aws s3 bucket setting on settings.py. Then, it's run with "python manage.py 0.0.0.0:8000".

Moreover, you can use 2 deployment methods,"manual deployment" and "docker-compolse deployment".
"docker-compolse deployment" is recommanded because you don't need to manually deploy the app 
running "python3 -m venv venv", "source venv/bin/activate", pip install -r requirements.txt" and so on.

---

The version "Python 3.8.5" is recommended to use but the above versions will be fine.
Don't run "python manage.py collectstaic" otherwise error occurs.

--- 

## You must do below for settings.py for 2 deployments:

Change "SECRET_KEY = 'abcdefg'" to different secret key for secure. <-- Line 12
(If you don't mind security, don't need to change 'abcdefg' which works properly)

Replace "EMAIL_HOST = 'smtp.gmail.com'" with your email host. <-- Line 123 (Needed for "Reset Password")

Replace "EMAIL_PORT = 587" with your email port. <-- Line 124 (Needed for "Reset Password")

Replace "EMAIL_HOST_USER = 'example@gmail.com'" with your email address. <-- Line 126 (Needed for "Reset Password")

Replase "EMAIL_HOST_PASSWORD = 'abcdefg'" with your email password. <-- Line 127 (Needed for "Reset Password")

---

## Option: 

If you use gmail, do 2 things below to get over very strong google's security:

1. Allow less secure apps: ON ↓↓↓
 
https://myaccount.google.com/lesssecureapps

2. Allow access to your Google account: ON (Tap "Continue")

https://accounts.google.com/DisplayUnlockCaptcha

---

When you run "pip install -r requirements.txt", one error will occur.
To solve it, run "pip install wheel".

After running "pip install -r requirements.txt", 
run "python manage.py migrate".

then, if you want to create a super user,
run "python manage.py createsuperuser".

Finally, run "python manage.py runserver 0.0.0.0:8000".
