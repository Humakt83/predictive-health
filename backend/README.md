
# Backend

Using docker file

***>cd to <repo_path>\predictive-health\backend***

docker build -t myimage . 

docker run -d --name mycontainer -p 5000:80 myimage



Browse to: http://localhost:5000


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
  
* ```
  pip install PyJWT
  ```
  

## On windows machine:

***>cd to <repo_path>\predictive-health\backend***

***>set FLASK_APP=%cd%\api\predictive.py***

***>set FLASK_ENV=development***

***>flask run***

 * Serving Flask app "<repo_path>\predictive-health\backend\api\predictive.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 309-333-800
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

### REST API

* / - GET

* /user/GET
* /user/POST
* /user/<id>/PUT
* /user/<id>/DELETE
* /users/GET

