
# Backend

Using docker file

1. ##### Start MongoDB database 

   ***>cd to <repo_path>\predictive-health\backend\db***

   Check ***stop_start.bat*** for docker commands.

2. ##### Start Flask container

   ***>cd to <repo_path>\predictive-health\backend***

   Check ***stop_start.bat*** for docker commands.



Browse to: http://localhost:5000/users



Alternative way (manual way)


Using python flask 

* Python 3.8.0

* ```pip install Flask-JSON
  pip install Flask
  ```

  ```
  pip install Flask-Cors
  ```
  
  ```
  pip install Flask-RESTFul
  ```
  
  ```
  pip install Flask-JSON
  ```
  
  ```
  pip install Flask-PyMongo 
  ```
  
* ```
  pip install PyJWT
  ```
  
  

## On windows machine:

***>cd to <repo_path>\predictive-health\backend***

***>set FLASK_APP=%cd%\app\main.py***

***>set FLASK_ENV=development***

***>flask run***

 * Serving Flask app "<repo_path>\predictive-health\backend\app\main.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 309-333-800
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

### REST API

* /users - GET                            # Returns list of all users

* /user/<user_id> - GET           # Data of one user

* /user/ - POST                          # Add new user

* /user/<user_id> - PUT           # Update existing user data

* /user/<user_id> - DELETE     # Delete user

  

* /user/<user_id>/poll - GET      # Get user poll data

* /user/<user_id>/poll - POST    # Add new user poll

* /user<user_id>/poll - DELETE  # Delete user poll data

  

* /user/<user_id>/prediction - GET      # Get user prediction data 

* /user/<user_id>/prediction - POST    # Add new user prediction (for development use)

* /user<user_id>/prediction - DELETE  # Delete user prediction data (for development use)

  

