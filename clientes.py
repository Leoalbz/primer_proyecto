class paciente:
    def __init__(self, nombre, raza, edad, diagnostico, tratamiento):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento

    def __str__(self):
        datos = { 
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
            print(f"Se agregó al paciente '{paciente.nombre}' a la lista de pacientes")

        def mostrar_pacientes(self):
            if self.paciente:
                print("Lista de pacientes:")
            for paciente in self.paciente:
                print(paciente)
            

pacientes = lista_pacientes()


pacientes.agregar_paciente(paciente("Tito","Bulldog","4","Intoxicacion por alimento inadecuado","comprimidos gastricos"))
pacientes.agregar_paciente(paciente("Maria","Persian","2","Sistitis","Inyectables + Comprimidos"))
pacientes.mostrar_pacientes()
