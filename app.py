from flask import Flask
from blueprints.front.home import home_bp
from extensions import configure_extensions
import logging
import sys

# Configurar logging para que se vea en la consola
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

app = Flask(__name__)

# Seguridad de información
app.config['SECRET_KEY'] = 'your_secret_key'

# Carpetas Imagenes
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads/imagenes'

# Carpetas Documentos
app.config['UPLOADED_DOCUMENTS_DEST'] = 'uploads/pdf'

# Carpeta para documentos Word
app.config['UPLOADED_WORD_DEST'] = 'uploads/word'

# Carpeta para documentos generados
app.config['GENERATED_UPLOADS_FOLDER'] = 'uploads/generated'

# Imágenes Config
configure_extensions(app)

# Blueprints modularizar código
app.register_blueprint(home_bp)

def print_startup_banner():
    """Imprime un banner de inicio de la aplicación"""
    print("\n" + "="*80)
    print("🚀 APLICACIÓN FLASK INICIADA")
    print("="*80)
    print("📁 Carpetas configuradas:")
    print(f"   - Imágenes: {app.config['UPLOADED_PHOTOS_DEST']}")
    print(f"   - Documentos: {app.config['UPLOADED_DOCUMENTS_DEST']}")
    print(f"   - Word: {app.config['UPLOADED_WORD_DEST']}")
    print(f"   - Generados: {app.config['GENERATED_UPLOADS_FOLDER']}")
    print("="*80)
    print("✅ Servidor listo para recibir solicitudes")
    print("🌐 Abre tu navegador en: http://127.0.0.1:5000")
    print("="*80 + "\n")

if __name__ == '__main__':
    print_startup_banner()
    app.run(debug=True, use_reloader=True)