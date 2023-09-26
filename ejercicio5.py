def validar_contrasena(contrasena):
    if len(contrasena) <8:
        return False
    uppercase= False
    lowercase = False
    digit=False
    for char in contrasena:
          if char.isupper():
             uppercase=True
          elif char.islower():    
             lowercase=True
          elif char.isdigit():
             digit=True
              
    return uppercase and lowercase and digit
    
contrasena1="fototeta"
contrasena2="ParkJimin28"
contrasena3="hola"
contrasena4="Jeffsaturn10"

print(validar_contrasena(contrasena1))
print(validar_contrasena(contrasena2))
print(validar_contrasena(contrasena3))
print(validar_contrasena(contrasena4))
    