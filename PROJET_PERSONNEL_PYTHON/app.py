from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(name)

app.secret_key = 'your secret key'

app.config['MYSQL_HOS000T'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Success@6623'
app.config['MYSQL_DB'] = 'projlogin'

mysql = MySQL(app)

# Route pour se connecter à la page login
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'admin@example.com' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

# Route pour se connecter au template register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form

        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route("/signup/",methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        nom = request.form['nom']
        prenom = request.form['prenom']
        mail = request.form['mail']
        p_word = request.form['pass']
        cpass = request.form['cpass']
        data_1 = User_et.query.filter_by(email=mail).first()
        if len(nom) < 4:
            flash('Nom doit etre superieur à 3 caractère', category='error')
        elif len(prenom) < 4:
            flash('Prénom doit etre superieur à 3 caractère', category='error')
        elif len(mail) < 6:
            flash('Adreese mail trop court', category='error')
        elif len(p_word) < 7:
            flash('Mot de passe trop court', category='error')
        elif p_word != cpass:
            flash('Mot de passe non conforme', category='error')
        elif data_1:
            flash('Ce email existe déjà', category='error')
        else:
            user = User_et(nom=nom, prenom=prenom, email=mail, p_word=p_word)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("acceuil"))
    return render_template("signup.html")
@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
