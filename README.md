Social Advisor
===============
This application is written in python3. Download app from github:

`git clone https://github.com/Dambre/social_advisor/

Install requirements file:

I suggest using `virtualenv create virtualenv --no-site-packages -p /usr/bin/python3 yourenv`

`source yourenv/bin/activate`

`pip install -r requirements.txt`
(if django syntax error occurs during install try uninstall django ; `run pip install --upgrade pip`; and install requirements again)

You can run app in dev mode by typing commands below:

You can use my SECRET_KEY or generate one yourself.

`export SECRET_KEY='(zooc&%peyw1*15o-c40q=^fhj_1h-1#x)(j7u&&_0+95=3s78'`

add local_settings.py file to hashbattle/ with twitter keys to auth

`python3.4 manage.py makemigrations`

`python3.4 manage.py migrate`

`python3.4 manage.py createsuperuser`

`python3.4 manage.py runserver --insecure`    (--insecure will serve static files when DEBUG=False)


Several urls:

http://127.0.0.1:8000/ basic battles table

http://127.0.0.1:8000/admin to access battle CRUD

API's:

http://127.0.0.1:8000/api/ generic battle view

http://127.0.0.1:8000/api/get-battle/{battle_id}/ get battle by ID user `curl -u user:password link`

Other:
`python3.4 manage.py update_hash`  -  update battles_scores
