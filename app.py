from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return render_template('index.html', name="Santhosh")

# Form page
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        username = request.form['username']
        return render_template('thanks.html', username=username)
    return render_template('form.html')

# API endpoint
@app.route('/api/data')
def api_data():
    return jsonify({
        "name": "Santhosh",
        "role": "DevOps Engineer",
        "location": "Hyderabad"
    })

# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
