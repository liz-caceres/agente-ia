import pandas as pd

# Simulación de datos de jubilados con información extendida
data = [
    {
        "nombre": "Ana Gómez",
        "edad": 67,
        "actividad": "Gimnasia",
        "antecedentes_medicos": "Hipertensión controlada",
        "contacto_emergencia": "Carlos Gómez - 11-5555-1111"
    },
    {
        "nombre": "Luis Fernández",
        "edad": 72,
        "actividad": "Yoga",
        "antecedentes_medicos": "Diabetes tipo 2",
        "contacto_emergencia": "María Fernández - 11-5555-2222"
    },
    {
        "nombre": "Marta López",
        "edad": 70,
        "actividad": "Caminata",
        "antecedentes_medicos": "Artrosis leve",
        "contacto_emergencia": "Jorge López - 11-5555-3333"
    },
    {
        "nombre": "Roberto Díaz",
        "edad": 75,
        "actividad": "Natación",
        "antecedentes_medicos": "Cardiopatía controlada",
        "contacto_emergencia": "Lucía Díaz - 11-5555-4444"
    },
    {
        "nombre": "Elena Martínez",
        "edad": 68,
        "actividad": "Taller de memoria",
        "antecedentes_medicos": "Sin antecedentes relevantes",
        "contacto_emergencia": "Pedro Martínez - 11-5555-5555"
    }
]

# Crear DataFrame con Pandas
df = pd.DataFrame(data)

# Mostrar los datos
print("Listado de jubilados con información extendida:\n")
print(df)

# Ejemplo de consulta: filtrar por actividad
print("\nJubilados que participan en Yoga:\n")
print(df[df["actividad"] == "Yoga"])
