# Pre-requisites

- Python
- pipenv
- postgres
- node / npm

### create a virtual environment
>> python -m pipenv install

### start with virtual env
>> pipenv shell

### install all the packages and file required 
>> pip install -r requirements.txt

### add the connection string of postgres
>> export SQLALCHEMY_DATABASE_URI="postgresql://{username}:{password}@{host_name}:{port}/{database_name}"


### import all the models
>> flask db
>> flask db init
>> flask db migrate
>> flask db upgrade

### add env varibales
>> export APP_SETTINGS="config.DevelopmentConfig"

### run the app
>> python app.py


### to check the info about the library and packages
>> https://requires.io/github/Afsaan/cargill-project/requirements/?branch=master

### to check the security vulnerability of all packages
>> safety check -r requirements.txt


### to start the node server
>> npm start
