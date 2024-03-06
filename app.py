from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from pyngrok import ngrok

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modele = LogisticRegression(max_iter=1000)
modele.fit(X_train, y_train)

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    longueur_sepale = float(request.args.get('longueur_sepale'))
    largeur_sepale = float(request.args.get('largeur_sepale'))
    longueur_petale = float(request.args.get('longueur_petale'))
    largeur_petale = float(request.args.get('largeur_petale'))
    prediction = modele.predict([[longueur_sepale, largeur_sepale, longueur_petale, largeur_petale]])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    ngrok_tunnel = ngrok.connect(port=5000)
    print('URL publique:', ngrok_tunnel.public_url)
    app.run(port=5000)
