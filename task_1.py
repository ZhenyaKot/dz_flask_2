# Создать страницу, на которой будет форма для ввода имени и электронной почты,
# при отправке которой будет создан cookie-файл с данными пользователя,
# а также будет произведено перенаправление на страницу приветствия,
# где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти»,
# при нажатии на которую будет удалён cookie-файл с данными пользователя
# и произведено перенаправление на страницу ввода имени и электронной почты.
from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('input_form.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        resp = make_response(redirect(url_for('welcome')))
        resp.set_cookie('username', username)
        resp.set_cookie('email', email)
        return resp


@app.route('/welcome')
def welcome():
    username = request.cookies.get('username')
    return render_template('welcome.html', username=username)


@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('username', '', expires=0)
    resp.set_cookie('email', '', expires=0)
    return resp


if __name__ == '__main__':
    app.run(debug=True)
