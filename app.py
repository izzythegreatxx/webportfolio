from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = 'static'
app.template_folder = 'templates'



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/projects', methods=['GET'])
def projects():
    return render_template('projects.html')



@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')



if __name__ =="__main__":
    app.run(host="0.0.0.0", port=80)
    