from flask import Flask
import settings
from views import router

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = settings.UPLOAD_FOLDER
app.secret_key = settings.SECRET_KEY
app.register_blueprint(router)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=settings.APP_DEBUG)