class Persona:

    def __init__(self, id, nombre, apellido, edad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def to_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad
        }