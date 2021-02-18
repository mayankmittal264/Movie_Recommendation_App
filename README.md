# Movie_Recommendation_App
Suggests Top 10 Movies which matches with Input Movie Name.

Step 1: First we’ll need to create a user who can login to the admin site. Run the following command:

$ python manage.py createsuperuser
Enter your desired username and press enter.

Username: ********
You will then be prompted for your desired email address:

Email address: ************
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

Password: **********
Password (again): *********
Superuser created successfully.

Step 2: Run the following commands -
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver

Step 3: open a Web browser and go to “/admin/” on your local domain – e.g., http://127.0.0.1:8000/admin/

Step 4: Enter your admin credentials and login

Step 5: create Movie database with details as Movie name, genre, Keyword and Poster

Step 6: open a Web browser and go to your local domai - e.g., http://127.0.0.1:8000

Step 7: Input any Movie name from your database and press enter. you can see all suggested movies list.
