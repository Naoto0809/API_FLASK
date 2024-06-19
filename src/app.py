import logging

from flask import Flask
from flask_cors import CORS
from config import config
from routes import Persona

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])

    # Configuración de logging
    logging.basicConfig(
        level=app.config['LOGGING_LEVEL'],
        format=app.config['LOGGING_FORMAT'],
        filename=app.config.get('LOGGING_FILE')
    )

    # Habilitar CORS desde el puerto 3000
    CORS(app, resources={"*": {"origins": "http://localhost:3000"}})
    
    # Registro de blueprints
    app.register_blueprint(Persona.main, url_prefix='/api/personas')

    # Manejador de errores personalizado
    @app.errorhandler(404)
    def page_not_found(error):
        logging.error(f"Error 404: {error}")  # Registrar el error
        return "<h1>Página no encontrada</h1>", 404

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
