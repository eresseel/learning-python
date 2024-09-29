# kulcs-ertek parok, dictionary

nevKor = {"alma": 1, "korte": 2, "szilva": 3}

for key in nevKor.keys():
    print(key)

for value in nevKor.values():
    print(value)

for key, value in nevKor.items():
    print(key, value)

dictionary = {"adat1": [1,2,3,4,5], "adat2": 33, "adat3": (6,7,8)}
for key, value in dictionary.items():
    print(key, value)

nevKor["szolo"] = 44
for key, value in nevKor.items():
    print(key, value)

nevKor.pop("korte")
for key, value in nevKor.items():
    print(key, value)

print(nevKor.get("alma"))

dictionary2 = { "adat1": {"kor": 14, "hajszin": "barna"},
                "adat2": {"kor": 14, "hajszin": "barna"},
                "adat3": {"kor": 14, "hajszin": "barna"} }

dictionary3 = { 1: {"kor": 14, "hajszin": "barna"},
                2: {"kor": 14, "hajszin": "barna"},
                3: {"kor": 14, "hajszin": "barna"} }