lang = "HUN"
if lang == "HUN":
    print("Jo estet")
elif lang == "ENG":
    print("Good evening")

lang = "ENG"
print("Jo estet") if lang == "HUN" else print("Good evening")
lang = "ESP"
print("Jo estet") if lang == "HUN" else (print("Good evening") if lang == "ENG" else print("Bueno noches"))