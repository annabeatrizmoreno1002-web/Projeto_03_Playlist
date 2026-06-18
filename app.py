import streamlit as st 

generos = {
    'Rock' : {
        'Raimundos' : 'https://www.youtube.com/watch?v=FkXWfreN2QA&list=RDFkXWfreN2QA&start_radio=1',
        'Raul Seixas' : 'https://www.youtube.com/watch?v=qcEfm7wJnUk&list=RDqcEfm7wJnUk&start_radio=1'
    },
    'Rock e folk alternativo' : {
        'Pitty' : 'https://www.youtube.com/watch?v=DP3j6hgS4VY&list=RDDP3j6hgS4VY&start_radio=1',
        'Rita lee' : 'https://www.youtube.com/watch?v=j_uJ8oYYl_U&list=RDj_uJ8oYYl_U&start_radio=1'
    },
    'Pagode samba' : {
        'Agepê' : 'https://www.youtube.com/watch?v=Y_YksQkHkgI&list=RDY_YksQkHkgI&start_radio=1',
        'Almir guineto' : 'https://www.youtube.com/watch?v=CTIvQ4KGtKM&list=RDCTIvQ4KGtKM&start_radio=1'
    },
    'Mpb ' : {
        'Vitroles' : 'https://www.youtube.com/watch?v=7fIBzHOQy5o&list=RD7fIBzHOQy5o&start_radio=1',
        'Chico Buarque' : 'https://www.youtube.com/watch?v=9y2xB90A0CY&list=RD9y2xB90A0CY&start_radio=1'
    }
}

st.sidebar.title('Raimundos')
st.sidebar.image('logo.png')

genero = st.sidebar.selectbox('Seleciona um genero musical', generos.keys())
artista = st.sidebar.selectbox('Selecione um artista', generos[genero].keys())

st.title(artista)
video, sobre =st.tabs(['Video','Sobre o artista'])

with video:
    st.video(generos[genero][artista])

with sobre:
    if artista == 'Raimundos':
        st.markdown('''Banda de rock conhecida por misturar peso, humor e influências nordestinas. Fez muito sucesso nos anos 90''')


    elif artista == 'Raul seixas':
        st.markdown('''Ícone do rock brasileiro, conhecido por sua criatividade, letras filosóficas e espírito rebelde. É chamado de "Maluco Beleza".''')
    elif artista == 'Raul Seixas':
        st.markdown('''Ícone do rock brasileiro, conhecido por sua criatividade, letras filosóficas e espírito rebelde. É chamado de "Maluco Beleza".
        Pitty-Cantora e compositora de rock conhecida por letras fortes, críticas e cheias de personalidade. Ficou famosa com músicas como Admirável Chip Novo e Máscara.
        Rita lee-Uma das maiores lendas do rock brasileiro. Misturava rock, humor e irreverência, sendo chamada por muitos de "Rainha do Rock Brasileiro"
        Agepê-Cantor de samba e pagode famoso por músicas românticas e pela voz marcante.
        Almir guineto-Um dos grandes nomes do samba e do pagode, ajudou a popularizar o banjo no samba moderno.
        Vitroles-Banda de rock com letras divertidas e nostálgicas, conhecida principalmente pela música Nova Demais Pra Mim''')
    elif artista == 'Chico Buarque':
        st.markdown('''Um dos compositores mais importantes do Brasil, famoso por letras poéticas, críticas sociais e músicas marcantes da MPB.''')

