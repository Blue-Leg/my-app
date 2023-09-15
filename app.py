from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el archivo
@app.route('/procesar', methods=['POST'])
def procesar_archivo():
    # Obtener los valores ingresados por el usuario desde el formulario
    back_x = float(request.form['back_x'])
    back_y = float(request.form['back_y'])
    back_z = float(request.form['back_z'])
    thigh_x = float(request.form['thigh_x'])
    thigh_y = float(request.form['thigh_y'])
    thigh_z = float(request.form['thigh_z'])

    # Luego, puedes usar estos datos para realizar la predicción con tu modelo entrenado
    datos = [[back_x, back_y, back_z, thigh_x, thigh_y, thigh_z]]  # Asegúrate de que estos datos estén en el formato correcto

    # Cargar el modelo entrenado de Random Forest Classifier
    modelo = joblib.load('modelo_random_forest.pkl')

    # Realizar la predicción utilizando el modelo
    prediccion = modelo.predict(datos)

    # En lugar de cargar el modelo aquí, debes cargarlo previamente antes de utilizar esta función.

    # La variable 'prediccion' ahora contiene el resultado de tu modelo

    # Puedes devolver este resultado a tu plantilla HTML para mostrarlo
    return render_template('index.html', resultado=prediccion)



if __name__ == '__main__':
    app.run(debug=True)

