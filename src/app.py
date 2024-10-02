from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from linkedin_profile_searcher import search_profile

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    name = request.form['name']
    summary, profile_pic_url = search_profile(name)
    print('tengo el summary, ahora armo la respuesta')
    return jsonify({
        'summary_and_facts': summary.to_dict(),
        'picture_url': profile_pic_url
    })

if __name__ == '__main__':
    app.run(debug=True)