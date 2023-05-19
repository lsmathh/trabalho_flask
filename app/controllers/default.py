from app import app, render_template
from app import db  
from app.models.tables import Alunos

from app.models.forms import LoginForm



@app.route('/<user>')
@app.route('/', defaults={"user": None})
def index(user):
    return render_template('index.html', user=user)


@app.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('login.html', form=form)


@app.route('/profile')
def profile():
    return "Hello world"



@app.route('/teste/<info>')
@app.route('/teste', defaults={'info': None})
def teste(info):
    r = Alunos.query.filter_by(name ="felipe").all()
    print(r)
    return 'ok'