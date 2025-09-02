@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name.capitalize()}!"
