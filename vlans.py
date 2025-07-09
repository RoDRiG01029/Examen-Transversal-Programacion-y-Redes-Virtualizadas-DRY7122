def verificar_vlan(vlan):
    if 1 <= vlan <= 1005:
        return "Esta VLAN pertenece al rango normal."
    elif 1006 <= vlan <= 4094:
        return "Esta VLAN pertenece al rango extendido."
    else:
        return "Esta VLAN esta fuera del rango válido."

try:
    vlan = int(input("Ingrese el número de VLAN: "))
    resultado = verificar_vlan(vlan)
    print(resultado)
except ValueError:
    print("Por favor, ingrese un número entero válido.")
