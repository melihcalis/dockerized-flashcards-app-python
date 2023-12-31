import random

countries_capitals = {"Türkiye": "Ankara", "Almanya": "Berlin", "Irak": "Bağdat", "Ermenistan": "Erivan", "Danimarka": "Kopenhag"}

coun_cap_length = len(countries_capitals)

keys_list = list(countries_capitals.keys())

#
while True:
    print("Yeni oyun!")
    score = 0
    random.shuffle(keys_list)
    for country in keys_list:
        answer = input( country + " adlı ülkenin başkenti neresidir?\n" )
        if countries_capitals.get(country).lower() == answer.lower():
            print("Doğru!")
            score += 1
        else : 
            print("Yanlış cevap")
    print("Skorunuz: "+str(score)+"\n")
#