import random
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma"
            }

for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        if word == "CRINGE":
            print(meme_dict["CRINGE"])

        if word == "LOL":
            print(meme_dict["LOL"])

        if word == "ROFL":
            print(meme_dict["ROFL"])
        
    else:
        print("esa palabra no existe")
