class paciente:
    def __init__(self, id, nombre, raza, edad, diagnostico, tratamiento):
        self.id = int(id)
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
                print("Lista de pacientes:")
            for paciente in self.paciente:
                print(paciente)
        
        def eliminar_paciente(self, paciente_id):
            for paciente in self.paciente:
                if paciente.id == paciente_id:
                    self.paciente.remove(paciente)
                    print(f"Se elimino al paciente {paciente.nombre} con Id {paciente.id} de la lista de pacientes\n")

pacientes = lista_pacientes()


pacientes.agregar_paciente(paciente(1,"Tito","Bulldog","4","Intoxicacion por alimento inadecuado","comprimidos gastricos"))
pacientes.agregar_paciente(paciente(2,"Maria","Persian","2","Cistitis","Inyectables + Comprimidos"))

pacientes.mostrar_pacientes()

pacientes.eliminar_paciente(2)

pacientes.mostrar_pacientes()
