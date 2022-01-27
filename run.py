# from flask import make_response, jsonify
from app import app, db
from app.models.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


# # @app.route("/")
# # def index():
# #     return make_response(jsonify({
# #         "message": "ok",
# #         "status": 200
# #     }), 200)

# # if __name__ == '__main__':
# #     app.run()
