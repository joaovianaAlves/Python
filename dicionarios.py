# person = {"nome": "Joao", "idade": 20}
# person = dict(nome= "Joao", idade= 20)
# person["telefone"] = "34434434"
# person["idade"] = 10
# person["telefone"] = "1391239103312"
# print(person)

people = {
    "joao": {"email": "joaovitorvianaalves@gmail.com", "idade": 20, "telefone": "232131541232"},
    "breno": {"email": "brenosilva@gmail.com", "idade": 28, "telefone": "2321315423112"},
    "andressa": {"email": "andressalima@gmail.com", "idade": 19, "telefone": "1325153451232"}
}

print(people["andressa"]["idade"])
print(people["joao"]["email"])

for person in people:
    print(person, people[person])

for person, valor in people.items():
    print(person, valor)
        