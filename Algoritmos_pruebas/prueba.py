# Algoritmo de prueba - Microservicio de Citas
# Taller Git - EPS

citas_ocupadas = ["08:00", "09:00", "10:30"]

nueva_cita = "11:00"

if nueva_cita in citas_ocupadas:
    print("Esa hora ya esta ocupada, elige otra")
else:
    citas_ocupadas.append(nueva_cita)
    print("Cita agendada a las " + nueva_cita)

print("Estas son las citas que hay hasta ahora:")
print(citas_ocupadas)

# probamos con una hora que ya existe
otra_cita = "09:00"

if otra_cita in citas_ocupadas:
    print("La hora " + otra_cita + " ya esta ocupada")
else:
    citas_ocupadas.append(otra_cita)
    print("Se agendo la cita")
