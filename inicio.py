import streamlit as st

# Nombre de la aplicación
st.title("Pesa tu vida - Tu Calculadora personal de peso")

#Barra lateral para la navegación entre páginas o despliegue
page = st.sidebar.selectbox("Selecciona una página:", ("Inicio", "App", "Contacto"))

# Página de inicio
if page == "Inicio":
    st.header("Bienvenido a pesa tu vida")
    st.write("¿No sabes cuantas calorias debes consumir?, con esta plataforma resolvemos tus dudas sobre calorias recomendadas según tu peso, estatura y género.")

    #Archivos multimedia
    st.image("calorias.png", caption="Imagen 1: calorias.png")
    st.image("balanza.png", caption="Imagen 2: balanza.png")

# Página de la calculadora de calorías
elif page == "App":
    st.header("Calculadora de calorías")
    st.write("Ingresa tus datos para calcular tus calorías diarias recomendadas.")

    # Entradas de usuario
    edad = st.slider("Edad", 1, 100, 25)
    peso = st.number_input("Peso (kg)", min_value=1.0, max_value=300.0, step=0.1)
    altura = st.number_input("Altura (cm)", min_value=1.0, max_value=300.0, step=0.1)
    género = st.radio("Género", ("Masculino", "Femenino"))

    # Cálculo de calorías
    if género == "Masculino":
        calorias = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * edad)
    else:
        calorias = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * edad)

    # Resultado de calorías recomendadas
        st.write(f"Calorías diarias recomendadas: {calorias:.2f} kcal")

# Página de contacto
elif page == "Contacto":
    st.header("Espero te haya servido esta información que te otorgamos")
    st.write("Integrantes: Constanza Gárate, Benjamín Gutiérrez y Paula Lazcano.")
    st.write("Curso: 4to Medio Green")
    st.image("pesa.png", caption="Imagen 3: pesa.png")
