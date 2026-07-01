from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', size='/size')

@app.route('/size/<int:num>')
def size(num):
    return render_template('lights.html', lights=f'/lights/{num}')

@app.route('/lights/<int:num>/<int:coef>')
def lights(num, coef):
    total = num + coef
    return render_template('electronics.html', electronics=f'/electronics/{total}')

@app.route('/electronics/<int:num>/<int:coef>')
def electronics(num, coef):
    total = num + coef
    return render_template('end.html', result=total)

if __name__ == '__main__':
    app.run(debug=True)
