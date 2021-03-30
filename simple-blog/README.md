---

simple-blog

"simple-blog" only has an app without other tools such as nginx, apache, 
gunicorn, settings for aws and azure and so on. Then, it's simply run with "python manage.py 0.0.0.0:8000".

Moreover, you can use 2 deployment methods,"manual deployment" and "docker-compolse deployment".
"docker-compolse deployment" is recommanded because you don't need to manually deploy the app 
running "python3 -m venv venv", "source venv/bin/activate", "pip install -r requirements.txt" and so on.

---




--- You must do for settings.py for any deployments -------------------------------

Change "SECRET_KEY = 'abcdefg'" to different secret key for secure. <-- Line 12
(If you don't mind security, don't need to change 'abcdefg' which works properly)

Replace "EMAIL_HOST = 'smtp.gmail.com'" with your email host. <-- Line 123 (Needed for "Reset Password")

Replace "EMAIL_PORT = 587" with your email port. <-- Line 124 (Needed for "Reset Password")

Replace "EMAIL_HOST_USER = 'example@gmail.com'" with your email address. <-- Line 126 (Needed for "Reset Password")

Replase "EMAIL_HOST_PASSWORD = 'abcdefg'" with your email password. <-- Line 127 (Needed for "Reset Password")

------------------------------------------------------------------------------------

--- Optional -----------------------------------------------------------------------

If you use gmail, do 2 things below to get over very strong google's security.

1. Allow less secure apps: ON ↓↓↓ 
https://myaccount.google.com/lesssecureapps

2. Allow access to your Google account: ON (Tap "Continue") ↓↓↓
https://accounts.google.com/DisplayUnlockCaptcha

------------------------------------------------------------------------------------

--- Snippet for manual deployment --------------------------------------------------

The version "Python 3.8.5" is recommended to use but the above versions will be fine.
"python manage.py collectstaic" is already run.
So don't run "python manage.py collectstaic" otherwise error occurs.

On ubuntu, run "pip install wheel" before running "pip install -r requirements.txt".
Otherwise, error will occur. 

After running "pip install -r requirements.txt""pip install -r requirements.txt", 
run "python manage.py migrate".

Then, create a super user running 
"python manage.py createsuperuser".

Finally, run "python manage.py runserver 0.0.0.0:8000".

-------------------------------------------------------------------------------------

--- Snippet for docker-compose deployment -------------------------------------------

There's already been "docker-compose.yml" and "dockerfiles" in this folder.

So just run "docker-compose up -d --build" for deployment.

Then run "docker-compose down -v --rmi" to remove all containers, volumes and images.

-------------------------------------------------------------------------------------
