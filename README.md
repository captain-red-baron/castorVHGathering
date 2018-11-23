# CastorVH - Data Gathering

Instructions for a UNIX based environment, tested on MAC OS X.

## General Setup
For all programming we use python 3.7 in an venv. 

1. Initialize the venv with `python3 -m venv castorvh-env`
1. Activate venv with `source castorvh-env/bin/activate`
1. Make sure upfront that cython is installed `pip install cython`
1. Install requirements with `pip install -r requirements.tct`

## Database
We are setting up a MS SQL Server 2017 through a docker image.

Prerequisits: Make sure you have installed [docker](https://www.docker.com) and have the docker daemon running.

### Set up Database with Docker
If you have already a MS SQL Server running, you can skip this step and modify the remaining commands.
1. Pull the docker image from MS: `sudo docker pull mcr.microsoft.com/mssql/server:2017-latest`
1. Run the container image: `sudo docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=<CastorVH!Passw0rd>' \
   -p 1433:1433 --name sqlCastor \
   -d mcr.microsoft.com/mssql/server:2017-latest`
1. Verify that your container image is running with `docker ps`

### Connect to the image with the Command Line tools and initialize tables
This is building up on the MS SQL Docker image we set up in the step before.

1. Connect to the container `sudo docker exec -it sqlCastor "bash"`
1. Once inside run sqlcmd: `/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P '<CastorVH!Passw0rd>'`
1. Create the Database we are about to use: `CREATE DATABASE CastorVH`, `SELECT Name from sys.Databases`, `GO`should show you the created database 

1. To get programmatically to the MS SQL instance, we need to install `brew install freetds` (only on mac, unix and windows should be good with just installing requirements)



1. Connect to the database with `sudo docker exec -it sqlCastor "bash"`
1. The sqlcmd cli should open up. 
