
# Configuración de la página en Streamlit
st.set_page_config(
    page_title="Chatbot Colectivo - Grupo de Clase",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Chatbot Colectivo - Grupo de Clase")
st.write("Este chatbot integra la información, gustos y personalidades de los 5 compañeros entrevistados.")

# Base de datos basada en las entrevistas del grupo
COMPANEROS_BD = {
    "aylen": {
        "nombre": "Aylen Ariana Angulo Arrieta",
        "edad": 15,
        "sexo": "Femenino",
        "musica": "Pop y Reggaetón",
        "peliculas": "Rápidos y Furiosos",
        "deportes": "Ninguno",
        "materia": "Español",
        "comida": "Arroz con pollo",
        "fortalezas": "Sinceridad y amabilidad",
        "deplicidades": "El amor"
    },
    "johan": {
        "nombre": "Johan Sebastian Céspedes Mendivelso",
        "edad": 16,
        "sexo": "Masculino",
        "musica": "Blessd y música urbana",
        "peliculas": "Spiderman",
        "deportes": "Fútbol",
        "materia": "Matemáticas",
        "comida": "Pizza",
        "fortalezas": "Fuerza y agilidad",
        "deplicidades": "El amor"
    },
    "kleiber": {
        "nombre": "Kleiber José Azuaje Marín",
        "edad": 16,
        "sexo": "Masculino",
        "musica": "Punk Rock",
        "peliculas": "Jurassic Park (1993)",
        "deportes": "Voleibol",
        "materia": "Física",
        "comida": "Lasaña",
        "fortalezas": "Inteligencia",
        "deplicidades": "El amor"
    },
    "juan": {
        "nombre": "Juan José Cruz Vargas",
        "edad": 16,
        "sexo": "Masculino",
        "musica": "Música variada",
        "peliculas": "Rápidos y Furiosos",
        "deportes": "Combate cuerpo a cuerpo",
        "materia": "Matemáticas",
        "comida": "Pasta",
        "fortalezas": "Intelecto y creatividad",
        "deplicidades": "La comida"
    },
    "keimer": {
        "nombre": "Keimer Jesús Gonzáles Inés",
        "edad": 17,
        "sexo": "Masculino",
        "musica": "Vallenato",
        "peliculas": "Rocky IV",
        "deportes": "Baloncesto",
        "materia": "Educación Física",
        "comida": "Pasta",
        "fortalezas": "Fuerza física",
        "deplicidades": "Nicol"
    }
}

def responder_pregunta(pregunta):
    pregunta_lower = pregunta.lower()
    
    # Preguntas sobre música / canciones
    if "musica" in pregunta_lower or "cancion" in pregunta_lower or "escucha" in pregunta_lower:
        return "Escuchamos géneros variados: Pop y Reggaetón (Aylen), Blessd (Johan), Punk Rock (Kleiber), Vallenato (Keimer) y música variada en general (Juan José)."
    
    # Preguntas sobre películas
    elif "pelicula" in pregunta_lower or "cine" in pregunta_lower:
        return "Nuestras películas favoritas son Rápidos y Furiosos (Aylen y Juan), Spiderman (Johan), Jurassic Park de 1993 (Kleiber) y Rocky IV (Keimer)."
    
    # Preguntas sobre deportes
    elif "deporte" in pregunta_lower or "entrena" in pregunta_lower:
        return "Entre el grupo practicamos Fútbol (Johan), Voleibol (Kleiber), Combate cuerpo a cuerpo (Juan José) y Baloncesto (Keimer)."
    
    # Preguntas sobre materias / estudio
    elif "materia" in pregunta_lower or "estudio" in pregunta_lower or "clase" in pregunta_lower:
        return "Nuestras materias favoritas son Matemáticas (Johan y Juan), Física (Kleiber), Español (Aylen) y Educación Física (Keimer)."
    
    # Preguntas sobre comida
    elif "comida" in pregunta_lower or "comer" in pregunta_lower:
        return "Nos encanta comer Arroz con pollo (Aylen), Pizza (Johan), Lasaña (Kleiber) y Pasta (Juan José y Keimer)."
    
    # Preguntas sobre integrantes
    elif "quienes" in pregunta_lower or "integrantes" in pregunta_lower or "compañeros" in pregunta_lower:
        return "El grupo está integrado por Aylen (15 años), Johan (16 años), Kleiber (16 años), Juan José (16 años) y Keimer (17 años)."
    
    # Respuesta por defecto / Personalidad combinada
    else:
        return "¡Hola! Soy la suma de la personalidad del grupo de programación. Nos apasionan los deportes, la pizza, la pasta, las matemáticas y escuchar desde Punk Rock hasta Vallenato. ¿De qué te gustaría hablar?"

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "audio" in message:
            st.audio(message["audio"], format="audio/mp3")

# Entrada del usuario
if prompt := st.chat_input("Escribe tu pregunta para el grupo..."):
    # Agregar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generar respuesta del bot
    respuesta_texto = responder_pregunta(prompt)

    # Generar audio con gTTS
    tts = gTTS(text=respuesta_texto, lang='es')
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)

    # Guardar y mostrar respuesta del asistente
    st.session_state.messages.append({
        "role": "assistant",
        "content": respuesta_texto,
        "audio": temp_file.name
    })
    
    with st.chat_message("assistant"):
        st.markdown(respuesta_texto)
        st.audio(temp_file.name, format="audio/mp3")
