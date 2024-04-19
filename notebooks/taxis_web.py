import streamlit as st
import pickle
import pandas as pd

# Cargar modelos
MODELOS = {
    "XGBoost": "modelo_xgb.pkl",
    "Gradient Boosting": "modelo_gb.pkl",
    "Random Forest": "modelo_rf.pkl"
}

@st.cache(allow_output_mutation=True)
def cargar_modelo(nombre_modelo):
    with open(nombre_modelo, 'rb') as archivo_modelo:
        modelo = pickle.load(archivo_modelo)
    return modelo

# Definir la clase InputData para validar los datos de entrada
class InputData:
    def __init__(self, HoraRecogida, diaSemana, mes, Borough_id):
        self.HoraRecogida = HoraRecogida
        self.diaSemana = diaSemana
        self.mes = mes
        self.Borough_id = Borough_id

# Definir la función de predicción
def predecir(modelo, data):
    # Extraer los valores de data
    hora_recogida = data.HoraRecogida
    diaSemana = data.diaSemana
    mes = data.mes
    borough_id = data.Borough_id

    # Crear un DataFrame con los valores extraídos
    input_data = pd.DataFrame({
        'HoraRecogida': [hora_recogida],
        'diaSemana': [diaSemana],
        'mes': [mes],
        'Borough_id': [borough_id]
    })

    # Convertir los datos de entrada a tipo float
    input_data = input_data.astype(float)

    # Realizar la predicción
    prediction = modelo.predict(input_data)

    # Devolver la predicción como JSON
    return {"Probabilidad de conseguir pasajero": prediction.tolist()}

def main():
    st.title("MoviPlus Estimator")

    # Selección del modelo
    modelo_seleccionado = st.selectbox("Seleccionar modelo:", list(MODELOS.keys()))

    # Cargar el modelo seleccionado
    modelo = cargar_modelo(MODELOS[modelo_seleccionado])

    # Entrada de datos
    st.subheader("Ingrese los datos para la predicción:")
    hora_recogida = st.number_input("Hora de recogida:", min_value=0, max_value=23, step=1)
    diaSemana = st.number_input("Dia de la semana:", min_value=1, max_value=7, step=1)
    mes = st.number_input("Mes:", min_value=1, max_value=12, step=1)
    borough_id = st.number_input("Borough ID:", min_value=0.0, step=1.0)

    # Realizar la predicción cuando se haga clic en el botón
    if st.button("Predecir"):
        # Crear objeto de datos de entrada
        input_data = InputData(HoraRecogida=hora_recogida, diaSemana=diaSemana, mes=mes, Borough_id=borough_id)

        # Realizar la predicción
        resultado = predecir(modelo, input_data)

        # Mostrar el resultado
        st.subheader("Resultado de la predicción:")
        st.json(resultado)

if __name__ == '__main__':
    main()
