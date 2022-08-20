def thesaurus(*names):
    aa = {}
    for name in names:
        key = name[0].capitalize()
        if key not in aa:
            aa[key] = []  
        aa[key].append(name)
    return aa

print(thesaurus("Иван", "Мария", "Петр", "Илья"))
