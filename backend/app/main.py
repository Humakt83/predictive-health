from datetime import datetime
from middlewares import login_required
from flask import Flask, request, redirect, url_for
from flask_json import FlaskJSON, JsonError, json_response
app = Flask(__name__)
FlaskJSON(app)

@app.route("/")
def hello():
    return "Hello World from Docker Flask"

@app.route("/user", methods=["GET"])
#@login_required
def user():
    now = datetime.utcnow()
    return json_response(status_ = 200, time = now)

@app.route("/user", methods=["POST"])
#@login_required
def create():
   #github_repo = GithubRepoSchema().load(json.loads(request.data))

   #if github_repo.errors:
   #  return json_response({'error': github_repo.errors}, 422)

   #kudo = Kudo(g.user).create_kudo_for(github_repo)
   #return json_response(data=request.data)
   return redirect(url_for('users'))

@app.route("/user/<int:user_id>", methods=["PUT"])
#@login_required
def update_user(user_id):
   #github_repo = GithubRepoSchema().load(json.loads(request.data))

   #if github_repo.errors:
   #  return json_response({'error': github_repo.errors}, 422)

   #kudo_service = Kudo(g.user)
   #if kudo_service.update_kudo_with(repo_id, github_repo):
   #  return json_response(github_repo.data)
   #else:
   return json_response(error = 'user not found', status_ = 404)

@app.route("/user/<int:user_id>", methods=["DELETE"])
#@login_required
def delete_user(user_id):
 #kudo_service = Kudo(g.user)
 #if kudo_service.delete_kudo_for(repo_id):
 #  return json_response({})
 #else:
   return json_response(error = 'user not found', status_ = 404)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)