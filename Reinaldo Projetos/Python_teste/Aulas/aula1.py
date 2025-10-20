"""Este código exibe as informaçõs do banco.json separadas, recebendo cada uma em uma string e exibindo
em loop continuo enquanto tiver dados"""

import json

file = "banco.json"

with open (file, "r") as json_file:
    data = json.load(json_file)
    name_data = (data["names"])
    for i in name_data:
        name = (i["firstname"])
        age = (i["age"])
        print (f"{name} is {age} ")

