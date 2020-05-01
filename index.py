from flask import Flask, render_template, url_for
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET KEY'] = '020132739904c9fbdfc4bd0394436925'

posts = [
    {
        'author' : 'Aj',
        'title' : 'Post 1',
        'content' : 'its my first one',
        'date_posted' : '12 August,2020',

    },
    {
        'author' : 'user',
        'title' : 'Post 2',
        'content' : 'its my second one',
        'date_posted' : '13 August,2020'
    }


]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts = posts)


@app.route("/about")
def about():
    return render_template('about.html',title = 'About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('registration.html', title = 'Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form=form)




if __name__=='__main__':
    app.run(debug=True)

