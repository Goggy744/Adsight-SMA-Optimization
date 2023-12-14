from flask import Flask


def createApp():
  #Create the application instance
  app = Flask(__name__)
  
  #Register the blueprint
  from .views import views
  app.register_blueprint(views, url_prefix="/")

  return app
