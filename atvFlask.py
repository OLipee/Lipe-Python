from flask import Flask


app = Flask(__name__)

@app.route('/decorator')
def ola_mundo():
    return 'é um comando que em determinada rota executa uma determinada funcao'

    
    
if __name__ == '__main__':
    app.run(debug=True)