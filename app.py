atributos = ("nome", "idade", "profissão" )


#lista dicionarios
usuarios = [
    {

        atributos[0]: "Ana Lopes",
        atributos[1]: 50,
        atributos[2]: "Busines International",
        
    },

    {   atributos[0]: "Cicrana Lopes",
        atributos[1]: 51,
        atributos[2]: "Busines International",
       
    },

    {
        atributos[0]: "Beltrana Lopes",
        atributos[1]: 51,
        atributos[2]: "Busines International",
        
    },
]

usuario = {}
for atributo in atributos:
        usuario[atributo] = input(f"informe o valor do campo {atributo}: ")
usuarios.append(usuario)

#exibir os dados de cada usuarios:

for usuario in usuarios:
    print("")
    for atributo in atributos:
        print(f"{atributo}: {usuario.get(atributo)}.")
        print("")


        
    
    
    
    
    
    
    
  


