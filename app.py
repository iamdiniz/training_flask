from flask import Flask, render_template, url_for, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.secret_key = 'minha-chave-teste'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return f'<User {self.username}>'

with app.app_context():
    db.create_all()
    try:
        if not User.query.filter_by(email='teste@email.com').first():
            user = User(
                username='usuarioteste',
                email='teste@email.com',
                password=generate_password_hash('123456')
            )
            db.session.add(user)
            db.session.commit()
            print('Usuário mockado criado!')
    except IntegrityError:
        db.session.rollback()
        print('⚠️ Usuário já existe.')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('home')) # Redireciona o navegador para acessar a rota /home (faz um novo request).
        else:
            return 'Credenciais inválidas!', 401
    return render_template('home.html')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    user = db.session.get(User, session.get('user_id'))
    if not user:
        return redirect(url_for('login'))
    return render_template('home.html', user=user) # Apenas renderiza o HTML do home.html, sem mudar de rota.

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0') # host para expor o servidor para fora do container