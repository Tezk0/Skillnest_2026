import json 

streamers = [
   {"nombre": "GameNinjaPro", "seguidores": 250000},
   {"nombre": "PixelWarrior", "seguidores": 180000}
]

streamers[0]["nombre"] = "otro valor"

print(streamers)

with open("./fundamentos/extras/streamers.json", "w") as archivo:
    json.dump(streamers, archivo)

with open("./fundamentos/extras/streamers.json", "r") as archivo:
    streamers_nuevos = json.load(archivo)

print("Nuevos streamers")
print(streamers_nuevos)