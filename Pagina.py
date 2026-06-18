import streamlit as st


st.set_page_config(
    page_title="Juan David Tejedor | Proyectos",
    page_icon=":briefcase:",
    layout="wide",
)


st.title("Juan David Tejedor Medina")
st.subheader("Portafolio de proyectos")

st.write(
    "Esta pagina esta lista para convertirse en tu portafolio personal de "
    "proyectos. Desde aqui puedes agregar secciones, enlaces, imagenes, "
    "dashboards y demos hechas con Streamlit."
)


with st.sidebar:
    st.header("Navegacion")
    seccion = st.radio(
        "Ir a",
        ["Inicio", "Proyectos", "Contacto"],
        label_visibility="collapsed",
    )


if seccion == "Inicio":
    st.markdown("### Bienvenido")
    st.write("Usa esta seccion para contar quien eres y que tipo de proyectos haces.")

elif seccion == "Proyectos":
    st.markdown("### Proyectos destacados")
    st.info("Agrega aqui tus proyectos, enlaces a repositorios, capturas y resultados.")

elif seccion == "Contacto":
    st.markdown("### Contacto")
    st.write("Agrega aqui tus redes, correo o formulario de contacto.")
