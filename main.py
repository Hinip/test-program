meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            "SHEESH": "ligera desaprobación"
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

        if word == "CREEPY":
            print(meme_dict["CREEPY"])

        if word == "AGGRO":
            print(meme_dict["AGGRO"])

        if word == "SHEESH":
            print(meme_dict["SHEESH"])
    
    else:
        print("esa palabra no existe")
