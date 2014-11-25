SBIR-EZ
========
[![Build Status](https://travis-ci.org/18F/afsbirez.svg?branch=master)](https://travis-ci.org/18F/afsbirez)

The SBIR-EZ (_sih-bur-easy_)project, provides a web service and user interface abstraction over the Small Business Innovation Research Program suite of tools used by SBIR.gov, DoDSBIR.com and various agency tools. The intent is that users may have a uniform interface to:

* Research existing and past SBIR solicitations
* Save opportunities for later processing
* Apply to opportunities independently of the owning agency
* Track the status of applications
* Receive and send communications
* View benchmarks

Please file issues at the [central repository for all Air Force Small Business repo](https://github.com/18f/afsmallbiz/issues?labels=Product%3A+SBIR&page=1&state=open)

### Installation
* Install PostGRESql
* Install Python 2.7
* Install virtualenv
* Checkout the source code and cd into it
```
$ git clone https://github.com/18F/afsbirez.git
$ cd afsbirez
```
* Make a virtualenv
```
$ mkdir env
$ virtualenv --no-site-packages ./env
```
* Activate the virtualenv
```
$ source env/bin/activate
```
you should now see (env) on your command prompt

* Install the latest [Node.js](http://nodejs.org/download/)
* Update NPM to the latest version 
```
$ npm install npm -g
```
* Install bower and grunt command line clients, as well as grunt dependencies
```
$ npm install
```

* Install Sass and Compass gems
```
$ gem install sass
$ gem install compass
```

* Perform default grunt tasks, including downloading the client side dependencies
```
$ grunt
```

### Configure the Database
Configure the pg_hba.conf file on your system (location varies) to allow local connections without passwords. Your hba.conf should have
lines like the below:
```
local   all             all                                     trust
host    all             all             127.0.0.1/32            trust
```

Create a database and role with your system user name
```
$ psql -c 'create role sbirez password 'sbirez';' -U postgres
$ psql -c 'CREATE DATABASE sbirezdev WITH OWNER sbirez;' -U postgres
```

Create the database tables on 'sbirezdev'
```
$ python manage.py db upgrade
```

### Running the Server using the Werkzeug built-in run_simple WSGI server. Please note that this is for
### development only.

```
$ python manage.py runserver
```

### Running Tests

First create a postgres database and test user

```
$ psql -c `create database sbireztest WITH OWNER sbirez;` -U postgres
```

Next, run the tests
```
$ python manage.py test
```

### License: Public Domain

This project is in the worldwide [public domain](LICENSE.md). As stated in [CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.
