from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return  render_template('index.html')
@app.route('/enigma1')
def index2():
    return  render_template('enigma.html')

@app.route('/enigma2')
def index3():
    return  render_template('enigma2.html')

if __name__ == '__main__':
    # O Render usa a variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
