import os
import settings
from flask import (
    Blueprint, 
    current_app,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    url_for
)
from middleware import model_predict
import utils

router = Blueprint('app_router', __name__, template_folder='templates')

@router.route('/', method=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # Render the index page
        return render_template('index.html')
    
    if request.method == 'POST':
        # Handle file upload or other POST actions
        if "file" not in request.files:
            flash('No file part in the request', 'error')
            return redirect(request.url)

        # Get file from the request 
        file = request.files.get('file')
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)

        # Check if the file is allowed, save it and make predictions 
        if file and utils.allowed_file(file.filename):
            file_hash = utils.get_file_hash(file)
            dst_filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], file_hash)

            if not os.path.exists(dst_filepath):
                file.save(dst_filepath) 
            flash('File successfully uploaded', 'success')
            prediction, score = model_predict(file_hash)
            context = {
                "prediction": prediction,
                "score": score,
                "filename": file_hash
            }
            return render_template("index.html", filename=file_hash, context=context)
        else:
            flash("Allowed image types are -> png, jpg, jpeg, gif", "error")
            return redirect(request.url) 

@router.route('/predict', methods=['POST'])
def predict():
    rpse = {
        "success": False,
        "prediction": None,
        "score": None
    }

    if "file" in request.files and utils.allowed_file(request.files["file"].filename):
        file = request.files["file"]
        file_hash = utils.get_file_hash(file)
        dst_filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], file_hash)
        if not os.path.exists(dst_filepath):
            file.save(dst_filepath)
        prediction, score = model_predict(file_hash)
        rpse["success"] = True
        rpse["prediction"] = prediction
        rpse["score"] = score
        return jsonify(rpse)
    
    return jsonify(rpse), 400