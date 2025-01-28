from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'company': 'Google',
        'location': 'Mountain View, CA',
        'salary': 'USD 100,000',
        'description': 'Work on the Google search engine'
    },
    {
        'id': 2,
        'title': 'Data Engineer',
        'company': 'Facebook',
        'location': 'Menlo Park, CA',
        'salary': 'USD 120,000',
        'description': 'Work on the Facebook social network'
    },
    {
        'id': 3,
        'title': 'Machine Learning Engineer',
        'company': 'Gojek',
        'location': 'Jakarta, Indonesia',
        'salary': 'USD 150,000',
        'description': 'Work on the Amazon e-commerce platform'
    }
]

@app.route("/")
def hello_sardi():
    return render_template('home.html', jobs=JOBS, company_name='Sardian')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)