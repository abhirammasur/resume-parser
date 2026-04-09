import os

if not os.path.exists('uploads'):
    os.makedirs('uploads')
import os
from flask import Flask, render_template, request, redirect
from config import Config
from models.db import db, Candidate
from parser.resume_parser import parse_resume

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    candidates = Candidate.query.all()
    return render_template('index.html', candidates=candidates)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['resume']

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        data = parse_resume(file_path)

        candidate = Candidate(
            name=data['name'],
            email=data['email'],
            skills=data['skills'],
            education=data['education']
        )

        db.session.add(candidate)
        db.session.commit()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
