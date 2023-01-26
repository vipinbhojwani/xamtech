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
   
        ```mysql -u root -p```

   2. Create database and seed it with sample dataset

        ```SOURCE <path-to sakilla/sakilla-schema.sql>
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

## References:
- Django setup: https://docs.djangoproject.com/en/4.1/topics/install/
- PyMySQL setup: https://stackoverflow.com/a/49893339
- Dataset: https://dev.mysql.com/doc/sakila/en/
- 
