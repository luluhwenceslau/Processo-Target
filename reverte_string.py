def inverter_string(string):
    caracteres = list(string)
    
    comprimento = len(caracteres)
    
    for i in range(comprimento // 2):
        caracteres[i], caracteres[comprimento - i - 1] = caracteres[comprimento - i - 1], caracteres[i]
    
    string_invertida = ''.join(caracteres)
    
    return string_invertida

string_original = input("Digite uma palavra para inverter: ")
string_invertida = inverter_string(string_original)
print(f"Palavra original:", string_original)
print(f"Palavra invertida:", string_invertida)
