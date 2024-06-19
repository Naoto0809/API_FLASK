from flask import Blueprint, jsonify 

#Modelos
from models.PersonaModel import PersonaModel

main = Blueprint('persona_blueprint', __name__)

@main.route('/')
def get_personas():
    try:
        persona_model = PersonaModel()
        personas = persona_model.get_personas()
        return jsonify(personas)
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
    
@main.route('/<id>')
def get_persona(id):
    try:
        persona_model = PersonaModel()
        persona = persona_model.get_persona(id)

        if persona is not None:
            return jsonify(persona)
        else:
            return jsonify({'error': 'No se encontró la persona'}), 404
        
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500