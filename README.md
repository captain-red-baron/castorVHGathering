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
1. Once inside run sqlcmd cli: `/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P '<CastorVH!Passw0rd>'`
1. Create the Database we are about to use: `CREATE DATABASE castor`, `SELECT Name from sys.Databases`, `GO`should show you the created database 

Now we should be able to connect to the MS SQL instance. If you are using a mac you need to do the following additionally:
1. install `brew install freetds` (only on mac, unix and windows should be good with just installing requirements)

Once the setup is done, we are running the `dll_statements.sql`, `college_seed.sql` and the `immunization_seed.sql` files with to seed the data. These files have been renamed from the original files:

1. `python3 database/seed_db.py`. Make sure that the `castorvh-env` virtual environment is activated.
