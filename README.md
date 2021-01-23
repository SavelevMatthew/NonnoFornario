![# CachingDNS](./github/logo.png)
> Pizza booking web application based on Django. It allows you to book a table, scroll menu as user. And manipulate with menu, tables and booking from admin panel.

## Table of Contents
[Installation](#local-installation)\
[Configuration](#configuration)\
[Administration](#administration)\
[Current State](#current-status)\
[Author](#author)

## Local Installation
Download project to your machine.
Then use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following packages.

```bash
pip install -r requirements.txt
```

## Configuration

Open **terminal** from project folder and type this commands (we use django-shortcuts):

#### This will check project for uninstalled migrations 
```bash
django mm
```
#### This command will install this migrations
```bash
django m
```

#### And finally, to run local server on **localhost:8000**
```bash
django r
```
Now you can access main page by visiting http://localhost:8000

## Administration
For being able to access admin panel (http://localhost:8000/admin), 
you must create account of superuser.

To do that, just type the command below and follow instructions:
```bash
django csu
```
Or you can use demo account as an example:\
login: admin\
password: hochupyat


## Current Status
Currently in active development

## Author
### Savelev Matvey
> #### Github: [@SavelevMatthew](https://github.com/SavelevMatthew)
> ##### Email: savelevmatthew@gmail.com
