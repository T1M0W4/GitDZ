
database = []

# {
# "id": "", 
# "firstName": "", 
# "lastName": "", 
# "birthDate": "", 
# "hiredDate": "", 
# "firedDate": "", 
# "position": "", 
# "salary": 0
# }

def new_employee(full_name: str, birth_date: str, position: str, salary: int):
    first_name, last_name = full_name.split(' ', 1)
    if salary <= 0:
        return{"id": -1, "errorDesc": "Salary not correct"}
    if not birth_date:
        return{"id": -1, "errorDesc": "Birth date not correct"}
    if not position:
        return{"id": -1, "errorDesc": "Position not correct"}    
    newcome = {
        "id": len(database), 
        "firstName": first_name, 
        "lastName": last_name, 
        "birthDate": birth_date, 
        "hiredDate": "eyrlytoday", 
        "firedDate": "", 
        "position": position, 
        "salary": salary
    }
    database.append(newcome)
    return{"id": newcome["id"], "errorDesc": ""}

def fire_employee(id: int):
    if 0 <= id < len(database):
        database[id]["firedDate"] = "today"
        return{"id": id, "errorDesc": ""}
    return {"id": -1, "errorDesc": "Id not correct"}

def get_employee(name: str):
    for x in database:
        if x["firstName"] == name:
            return x["id"]
        

r1 = new_employee("Тимур Шагимарданов", "1966-07-1", "разработчик ПО", 1500050)
r2 = new_employee("Алмат Утенов", "1975-03-11", "разработчик ПО", 1750050)
r3 = new_employee("Александр Нежельский", "2001-11-23", "СТО", 25500050)
r4 = new_employee("Санния Бектасова", "2005-09-14", "СЕО", 50000000)
r5 = new_employee("Аргын Ликеров", "1995-05-29", "cos", 10)
r5 = fire_employee(4)

print(database)