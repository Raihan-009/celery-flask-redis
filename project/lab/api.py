from run import app
from project import tasks

@app.route('/add')
def add():
    val = tasks.add.delay(5,6)
    result = val.get()
    return f'Hello, World!, {result}'


@app.route('/sub')
def sub():
    val = tasks.sub.delay(5,6)
    result = val.get()
    return f'Hello, World!, {result}'

@app.route('/about')
def about():
    return 'About Us'