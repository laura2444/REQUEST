ReQuest
ReQuest es una aplicación web desarrollada en Python y Flask que permite a los usuarios cargar sus historias de usuario en formato txt, Word o PDF y automáticamente convertirlas en requisitos, clasificándolas por tipo y prioridad mediante integración con la API de Gemini.

Características principales
Subida de archivos en formatos txt, Word o PDF.
Conversión automática de historias de usuario en requisitos.
Clasificación de requisitos por categorías y prioridad.
Interfaz limpia y moderna basada en Tailwind CSS.
Responsive: usable desde computadoras, tablets y dispositivos móviles.
Descarga de resultados en Word, PDF o TXT.
Tecnologías
Python 3.x
Flask
Tailwind CSS
Jinja2 (templating)
Gemini API (procesamiento de historias de usuario)
HTML5 / CSS3 / JavaScript
Boxicons para íconos
Instalación y ejecución
Clona el repositorio, crea y activa un entorno virtual, instala las dependencias y ejecuta la aplicación con un solo bloque de comandos:

# Clonar el repositorio
git clone https://github.com/TU_USUARIO/NOMBRE_DEL_REPO.git
cd NOMBRE_DEL_REPO

# Crear y activar el entorno virtual
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Crear archivo de variables de entorno .env con tu API key de Gemini
echo "GEMINI_API_KEY=tu_api_key" > .env

# Ejecutar la aplicación
python app.py