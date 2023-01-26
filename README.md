## About this project
This is an assignment project which is developed in Python using Django framework, MySQL database.
The objective was to expose a GraphQL api that queries a data set loaded in a MySQL.

For sample dataset around films, a sample MYSQL database (Sakila)[https://dev.mysql.com/doc/sakila/en/] was used.

The instructions to setup and test are added below.


## How to setup?
### Pre-requisite
1. MySQL Server and CLI should be installed. 
To install follow: https://dev.mysql.com/downloads/mysql/

### Steps
1. Create and activate Python virtual env:
   ```
   python3 -m venv xvenv
   source xvenv/bin/activate
   ```

2. Install pip dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create database and import seed data:
   1. Login to MySQL monitor
   
        ```
        mysql -u root -p
        ```

   2. Create database and seed it with sample dataset

        ```
           SOURCE <path-to sakilla/sakilla-schema.sql>
           SOURCE <path-to sakilla/sakilla-data.sql>
           quit;
        ```

4. Run `migrate` to create other tables
    ```
    python manage.py migrate
    ```

5. Run server
   ```
   ./manage.py runserver
   ```

## How to Test?
1. Once server is started, navigate to http://127.0.0.1:8000/graphql

2. Sample GraphQL query to get a film:
   ```
   {
      film(id: 101) {
         filmId
         title
         rentalRate
         specialFeatures
      }
   }
   ```

3. Sample GraphQL query to get list of films:
   ```
   query {
      films(offset: 51, limit: 5) {
         filmId
         title
         rentalRate
         specialFeatures
      }
   }

   ```

## References:
- Django setup: https://docs.djangoproject.com/en/4.1/topics/install/
- PyMySQL setup: https://stackoverflow.com/a/49893339
- Dataset: https://dev.mysql.com/doc/sakila/en
