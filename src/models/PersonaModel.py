import logging

from database.db import get_connection
from .entities.Persona import Persona

class PersonaModel():

    @classmethod
    def get_personas(self):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT id, nombre, apellido, edad FROM personas')
                resultset = cursor.fetchall()
                personas = []
                for row in resultset:
                    persona = Persona(row[0], row[1], row[2], row[3])
                    personas.append(persona.to_json())
                logging.debug(f"Se obtuvieron {len(personas)} personas")
                return personas
        except Exception as ex:
            logging.error(f"Error al obtener las personas: {ex}")
            raise Exception(ex)

    @classmethod
    def get_persona(self, id):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT id, nombre, apellido, edad FROM personas WHERE id = %s', (id,))
                row = cursor.fetchone()
                if row is not None:
                    persona = Persona(row[0], row[1], row[2], row[3]).to_json()
                    logging.debug(f"Se obtuvo la persona con ID {id}")
                    return persona
                else:
                    logging.warning(f"No se encontró la persona con ID {id}")  # Cambiamos a warning
                    return None
        except Exception as ex:
            logging.error(f"Error al obtener la persona con ID {id}: {ex}")
            raise Exception(ex)