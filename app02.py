from flask import Flask, make_response, redirect, request, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        response = make_response(redirect(url_for('hello')))
        name = request.form.get('name')
        email = request.form.get('mail')
        response.set_cookie('username', name)
        response.set_cookie('email', email)
        return response
    if 'username' in request.cookies:
        return redirect(url_for('hello'))
    else:
        return render_template('index.html')

@app.route('/hello/')
def hello():
    name = request.cookies.get('username')
    email = request.cookies.get('email')
    if name:
        mas = {'name': name, 'email': email}
        return render_template('hello.html', **mas)
    return redirect(url_for('root'))

@app.route('/logout/')
def logout():
    res = make_response(redirect(url_for('root')))
    res.set_cookie('username', '', max_age=0)
    res.set_cookie('email', '', max_age=0)
    return res

if __name__ == '__main__':
    app.run()