<h1 align="center">Django Smart RFID Entrance Control</h1>
<h3 align="center">this is a simple example of communication between RFID gateway and server </h3>
<p align="center">
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.djangoproject.com/" target="_blank"> <img src="https://user-images.githubusercontent.com/29748439/177030588-a1916efd-384b-439a-9b30-24dd24dd48b6.png" alt="django" width="40" height="40"/> </a>
<a href="https://www.django-rest-framework.org/" target="_blank"> <img src="https://www.django-rest-framework.org/img/logo.png" alt="sqlite" width="90" height="40"/> </a>
<a href="https://www.django-rest-framework.org/" target="_blank"> <img src="https://www.postgresql.org/media/img/about/press/elephant.png" alt="Postgresql" width="40" height="40"/> </a>
<a href="https://www.nginx.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nginx/nginx-original.svg" alt="nginx" width="40" height="40"/> </a>
<a href="https://www.docker.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a>
<a href="https://getbootstrap.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a>
<a href="https://www.w3.org/html/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
</a>

</p>


### Overview
- [Overview](#overview)
- [demo](#demo)
- [Features](#features)
- [Setup](#setup)
  - [Build everything:](#build-everything)
- [options](#options)
- [Reformat and check](#reformat-and-check)
- [Database schema](#database-schema)
- [Bugs or Opinion](#bugs-or-opinion)


### demo
<p align="center">
<img src="" width="500"/>
</p>

### Features
- Django LTS
- Class Based views (ApiView)
- Django RestFramework
- User authentication
- Black
- Flake8
- Responsive Design
- Bootstrap5
- heroku




### Setup
To get this repository, run the following command inside your git enabled terminal
```bash
git clone https://github.com/AliBigdeli/Django-Smart-RFID-Control.git
```

#### Build everything:

The first time you run this it's going to take 5-10 minutes depending on your
internet connection speed and computer's hardware specs. That's because it's
going to download a few Docker images and build the Python + requirements dependencies.*


For Development:
```sh
docker compose up --build -d
```

For Actual Usage:
```sh
docker compose -f docker-compose-stage.yml up --build -d
```


Once the server is up and running, head over to http://127.0.0.1:8000  if you ran it in dev mode or else use your localhost or the server ip address for the App.
### options
Project it self has the user creation form but still in order to use the admin you need to create a super user.you can use the createsuperuser option to make a super user.
```bash
docker compose -f docker-compose-stage.yml exec backend  sh -c "python manage.py createsuperuser"
```



### Reformat and check
If you want your code to be check by pep8 and all the guide lines, there are two packages added to requirements in order to check and reformat code.
you can use it by this command:
```bash
black -l 79 . && flake8
```

### Database schema
A simple view of the project model schema.
<p align="center">
<img src="" alt="database schema" width="600"/>
</p>


### Bugs or Opinion
Feel free to let me know if there are any problems or any request you have for this repo.
