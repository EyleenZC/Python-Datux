class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []  # Lista de horas asignadas al conductor

    def asignar_horario(self, hora):
        if hora in self.horarios:
            print(f"El conductor {self.nombre} ya tiene asignado el horario {hora}:00.")
        else:
            self.horarios.append(hora)
            print(f"Horario {hora}:00 asignado al conductor {self.nombre}.")

class Bus:
    def __init__(self, placa):
        self.placa = placa
        self.ruta = None
        self.horarios = []
        self.conductor = None

    def asignar_ruta(self, ruta):
        self.ruta = ruta
        print(f"Ruta {ruta} asignada al bus {self.placa}.")

    def registrar_horario(self, hora):
        if hora in self.horarios:
            print(f"El bus {self.placa} ya tiene registrado el horario {hora}:00.")
        else:
            self.horarios.append(hora)
            print(f"Horario {hora}:00 registrado para el bus {self.placa}.")

    def asignar_conductor(self, conductor, hora):
        if self.conductor and hora in self.conductor.horarios:
            print(f"Error: El conductor {conductor.nombre} ya tiene un bus asignado en ese horario.")
        else:
            self.conductor = conductor
            conductor.asignar_horario(hora)
            print(f"El conductor {conductor.nombre} ha sido asignado al bus {self.placa} en el horario {hora}:00.")

class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, placa):
        bus = Bus(placa)
        self.buses.append(bus)
        print(f"Bus con placa {placa} agregado correctamente.")

    def agregar_conductor(self, nombre):
        conductor = Conductor(nombre)
        self.conductores.append(conductor)
        print(f"Conductor {nombre} agregado correctamente.")

    def menu(self):
        while True:
            print("\nMenú de Gestión de Buses:")
            print("1. Agregar bus")
            print("2. Agregar ruta a bus")
            print("3. Registrar horario a bus")
            print("4. Agregar conductor")
            print("5. Agregar horario a conductor")
            print("6. Asignar bus a conductor")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                placa = input("Ingrese la placa del bus: ")
                self.agregar_bus(placa)
            elif opcion == "2":
                placa = input("Ingrese la placa del bus: ")
                ruta = input("Ingrese la ruta: ")
                bus = next((b for b in self.buses if b.placa == placa), None)
                if bus:
                    bus.asignar_ruta(ruta)
                else:
                    print("Bus no encontrado.")
            elif opcion == "3":
                placa = input("Ingrese la placa del bus: ")
                hora = int(input("Ingrese el horario (0-23): "))
                bus = next((b for b in self.buses if b.placa == placa), None)
                if bus:
                    bus.registrar_horario(hora)
                else:
                    print("Bus no encontrado.")
            elif opcion == "4":
                nombre = input("Ingrese el nombre del conductor: ")
                self.agregar_conductor(nombre)
            elif opcion == "5":
                nombre = input("Ingrese el nombre del conductor: ")
                hora = int(input("Ingrese el horario (0-23): "))
                conductor = next((c for c in self.conductores if c.nombre == nombre), None)
                if conductor:
                    conductor.asignar_horario(hora)
                else:
                    print("Conductor no encontrado.")
            elif opcion == "6":
                nombre = input("Ingrese el nombre del conductor: ")
                placa = input("Ingrese la placa del bus: ")
                hora = int(input("Ingrese el horario (0-23): "))
                bus = next((b for b in self.buses if b.placa == placa), None)
                conductor = next((c for c in self.conductores if c.nombre == nombre), None)
                if bus and conductor:
                    bus.asignar_conductor(conductor, hora)
                else:
                    print("Bus o conductor no encontrado.")
            elif opcion == "7":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intente nuevamente.")

# Ejecutar el programa
admin = Admin()
admin.menu()
