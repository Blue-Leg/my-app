from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el archivo
@app.route('/predict', methods=['POST'])
def procesar_archivo():
    # Obtener los valores ingresados por el usuario desde el formulario
    back_x = float(request.form['back_x'])
    back_y = float(request.form['back_y'])
    back_z = float(request.form['back_z'])
    thigh_x = float(request.form['thigh_x'])
    thigh_y = float(request.form['thigh_y'])
    thigh_z = float(request.form['thigh_z'])

    # Guardar los datos del formulario
    datos = [[back_x, back_y, back_z, thigh_x, thigh_y, thigh_z]]
    print(datos)

    # Cargar el modelo entrenado de Random Forest Classifier
    modelo = joblib.load('modelo_random_forest.joblib')

    # Realizar la predicción utilizando el modelo
    prediccion = modelo.predict(datos)
    
    #Mostrar el tipo de actividad dependiendo de la predicción
    if prediccion == 1:
        actividad = "Walking / Caminando"
    elif prediccion == 3:
        actividad = "Shuffling / Arrastrar los pies"
    elif prediccion == 4: 
        actividad = "Stairs (Ascending) / Subir escaleras"
    elif prediccion == 5:
        actividad = "Stairs (Descending) / Bajar escaleras"
    elif prediccion == 6:
        actividad = "Standing / Estar parado"
    elif prediccion == 7:
        actividad = "Sitting / Estar sentado"
    else:
        actividad = "Lying / Estar acostado"

    return render_template('index.html', resultado=actividad)

if __name__ == '__main__':
    app.run(debug=True)

