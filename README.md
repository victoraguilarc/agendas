## Agendas


![styleguide](https://img.shields.io/badge/styleguide-flake8-blue)
![Coverage](web/badges/coverage.svg) 


#### Features

  - [x] Registration
  - [x] Autthentication
  - [x] Support for Facebook and  Google(TODO).
  - [x] Appointment Booking
  - [x] Appointments Review
   
### Technologies

  * [Django](https://www.djangoproject.com/)
  * [Django Rest Framework](http://www.django-rest-framework.org/)
  * [VueJS](https://vuejs.org/)
  
### Run locally (for development)
First you need to have installed `git`, `docker`, `ssh`, `make` and and a good `terminal`.

  1. `git clone git@github.com:victoraguilarc/agendas.git`
  2. [Download](https://drive.google.com/file/d/1slmIV_BTrkt7AdlC37lGLJ0cAxnv7YCe/view?usp=sharing) `.envs` folder and put it in the root of project, it contains `dev`, `test` subfolders with a layout of the environment variables. 
  3. `make build` builds the images for development. 
  4. `make migrate` creates database and tables 
  5. `make fixtures` loads testing data.
  6. `make up` runs development server at `http://localhost:8000`
  
### Other useful commands
  * `make debug` enable deebugging server `debug`.
  * `make migrations` run django makemigrations command
  * `make migrate` run django migrate command
  * `make superuser` make a superuserfor develoment
  * `make isort` Fix posible import issues
  * `make test` Run the tests with pytest
  * `make locales` Generate translation files
  * `make compile_locales` Compile translation files

### Frontend development

This projeect contains minimal frontend to some transactional fallback windows specially.
If you want to use it, run the following commands:

  * `npm install --global gulp-cli` Install gulp
  * `npm install` Install nodejs dependencies
  * `gulp` generate `css`, `js`  production files.
   
