class paciente:
    def __init__(self, id, nombre, raza, edad, diagnostico, tratamiento):
        self.id = id
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento

    def __str__(self):
        datos = { 
            "Id": self.id,
            "Nombre": self.nombre,
            "Raza": self.raza,
            "Edad": self.edad,
            "Diagnóstico": self.diagnostico,
            "Tratamiento": self.tratamiento
        }
          
        formato_salida = ""
        for key, value in datos.items():
            formato_salida += f"{key}: {value}\n"
        return formato_salida

class lista_pacientes:
    def __init__(self):
        self.paciente = []
  
    def agregar_paciente(self, paciente):
        self.paciente.append(paciente)
        print(f"Se agregó al paciente '{paciente.nombre}' a la lista de pacientes\n")

    def mostrar_pacientes(self):
        if self.paciente:
            datos = "\n".join(str(paciente) for paciente in self.paciente) 
        else:
            datos = "No hay pacientes en la lista"
        return datos
        
    def eliminar_paciente(self, paciente_id):
        for paciente in self.paciente:
            if paciente.id == paciente_id:
                self.paciente.remove(paciente)
                print(f"Se elimino al paciente {paciente.nombre} con Id {paciente.id} de la lista de pacientes\n")
                return
            
        print(f"No se encontró ningún paciente con Id {paciente_id}")

