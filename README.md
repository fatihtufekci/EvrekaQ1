# EvrekaQ1
------------------------------
## Project Setup

First, run the following command.
```
sudo apt install python3-pip python3-dev python3-django python3-virtualenv
```

Run the following command to download the project.

```
git clone https://github.com/fatihtufekci/EvrekaQ1.git
```

Run the following commands in order to install the virtual environment.
```sh
virtualenv -p python3 venv
source venv/bin/activate
```

Run the following command to install the required packages.

```sh
pip3 install -r requirements.txt 
```

If it gave an error in the above step;
```sh
pip3 install Django
pip3 install python-dotenv
pip3 install djangorestframework
pip3 install psycopg2
pip3 install django_extensions
pip3 install ipython
```

- **Create your .env file as in .env.sample**

Run the code below to create the database.

```sh
python3 manage.py makemigrations
python3 manage.py migrate
```

To connect to the admin panel that we will use to add records to our models, run the command below and create a user.

```sh
python3 manage.py createsuperuser
```

Run the following command to boot the project.
```
python3 manage.py runserver
```

Enter the admin panel from the link below and add records to vehicle and navigation models.
[http://localhost:8000/admin/](http://localhost:8000/admin/)


You can reach the project from the link below.
[http://localhost:8000/navigation-record/](http://localhost:8000/navigation-record/)

---------------------


## Project Structure
- In our project, we have two models named navigation record and vehicle.
- Our NavigationRecordSerializer serializer, which provides communication between Python data structure and json format, has been created.
- A view that allows us to perform CRUD operations has been created.
- The get_last_points() method was written in the Manager class of our NavigationRecord model.
- In our get_last_points() method, the last navigation data from the last 48 hours is returned for each vehicle.
- API Tests written.

