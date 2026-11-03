import streamlit as st
from dados_api import previsao_temperatura

# Cidades
cidades = {
    "Santana de Parnaiba" : [50.43744063143905, 4.673393387951432],
    "Barueri": [-23.502544132720764, -46.87880724047182],
    "França" : [46.67168911057337, 2.5842399620455874],
    "Irlanda" : [54.68512219839647, -6.744846075627137],
    "Canadá" : [60.41936772932658, -112.77936721354261],
}

# ------------------------ SIDEBAR
st.sidebar.title("previsão do tempo")
st.sidebar.image("logo.png")

cidade = st.sidebar.selectbox("Escolha a cidade:", cidades.keys())
latitude , longitude = cidades[cidade]

# ---------------------- BODY
st.title(f' Previsão do tempo em {cidade} para os proximos 7 dias')

st.markdown("---")

# Previsão de temperatura
dados, temperatura_media = previsao_temperatura(latitude, longitude)

for i, d in temperatura_media.iterrows():

    with st.container(border=True):
        st.subheader(d['dia_semana'])

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Data",f'{int(d['dia'])}/{int(d['mes'])}')

        with col2:
            st.metric("Temperatura média", f"{d['temperatura_media']:.2f}°")

            with col3:
                if d['temperatura_media'] < 10:
                    temp = "cold.png"

                elif d['temperatura_media'] < 18:
                    temp = "cold.png"

                elif d['temperatura_media'] < 25:
                    temp = "warm.png"

                else:
                    temp = "comfort.png"

                st.image(temp, width=400)