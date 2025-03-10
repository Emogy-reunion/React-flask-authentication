'''
initializes the libraries
creates initial admins
runs the application
'''
from create_app import create_app
from routes.authentication import auth
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from routes.verification import verify
from routes.reset_password import reset


app = create_app()
jwt = JWTManager(app)

app.register_blueprint(auth)
app.register_blueprint(verify)
app.register_blueprint(reset)

if __name__ == '__main__':
        app.run(debug=True)
