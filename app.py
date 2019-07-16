from flask import Flask,url_for
app=Flask(__name__)
@app.route('/')
def hello():
    #return 'Welcome to My Watchlist!'
    return '<h2>Hello DuXin!</h2><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
    return 'User:%s ' %name

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page',name='ChenPengKang'))
    print(url_for('user_page',name='DuXin'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for',num=2))
    return 'Test page'