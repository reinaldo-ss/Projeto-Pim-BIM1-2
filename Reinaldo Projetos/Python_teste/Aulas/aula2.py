"""Este código acrescenta dados a uma lista apartir de uma inserção no código
ele identa automaticamente em 4 linhas, acredito que caso tivesse mais
voce poderia identar mais linhas pra que ele construisse no mesmo padrão sem baguçar
a formatação."""

import json

def write_json(data, filename="banco.json"):
    with open (filename, "w") as f:
        json.dump(data, f, indent=4)

with open ("banco.json") as json_file:
    data = json.load(json_file)
    temp = data["names"]
    y = {"firstname:": "Joe", "age": 40}
    temp.append(y)

write_json(data)