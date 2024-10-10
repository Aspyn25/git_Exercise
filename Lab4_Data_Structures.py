import numpy as np

student = {
    "Alice" : [85, 78, 92],
    "Bob" : [79, 74, 81],
    "Charlie" : [91, 82, 85],
    "David" : [76, 85, 83],
    "Eve" : [88, 79, 92]
}
aver_grade = [(k, sum(v)/len(v)) for k,v in student.items()]
print(aver_grade)

highest = max(aver_grade, key=lambda x: x[1]) # compared with average score
lowest = min(aver_grade, key=lambda x: x[1])

print(f"{highest[0]} got the highest average Score as {highest[1]:.2f}.")
print(f"{lowest[0]} got the lowest average Score as {lowest[1]}.")

student["Frank"] = [80,90,85]
print(student)

print("-------2-------")

inventory = {
    "apple" : (50,0.5),
    "banana" : (100, 0.2),
    "orange" : (75, 0.3),
    "pear" : (20, 0.4)
}

for k, v in inventory.items():
    print(f"{k}'s quantity is {inventory[k][0]} and each price is ${inventory[k][1]}.")
inventory["mango"] = 30,0.6
inventory["banana"] = 120,0.2
del(inventory["pear"])
print(inventory)

print("-------3-------")

employees = [
("John Doe", "Accounting", "john.doe@example.com"),
    ("Jane Smith","Marketing", "jane.smith@example.com"),
    ("Emily Davis", "HR", "emily.davis@example.com"),
    ("Michael Brown", "IT", "michael.brown@example.com") ]
task2 = []
for x, y, z in employees:
    print(f"name : {x}, department : {y}")
    task2.append((x.split()[1], z))

task2 = sorted(task2)
for y in task2:
    print(y[1])

employees.append(("David Wilson", "Sales", "david.wilson@example.com"))
print(employees)

for x in employees:
    if x[0] == "Jane Smith":
        print(x[1])

print("-------4-------")
library = {
    "978-3-16-148410-0": {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
    "978-0-14-028329-7": {"title": "1984", "author": "George Orwell", "year": 1949},
    "978-0-7432-7356-5": {"title": "To Kill a Mockingbird", "author": "Harper Lee","year": 1960},
    "978-0-452-28423-4": {"title": "Brave New World", "author": "Aldous Huxley","year": 1932} }

for k, v in library.items():
    print(f"\"{k}\" is the book's ISBN, name is \"{library[k]['title']}\", author is \"{library[k]['author']}\", and year \"{library[k]['year']}\".")

for k, v in library.items():
    if k == "978-0-14-028329-7":
        print(f"\"{k}\" is the book's ISBN, name is \"{library[k]['title']}\", author is \"{library[k]['author']}\", and year \"{library[k]['year']}\".")

library["978-1-4028-9462-6"] = {"title": "The Great Gatsby",
                                "author": "F. Scott Fitzgerald",
                                "year": 1925}

library["978-0-7432-7356-5"]["year"] = 1961
print(library)

del(library["978-0-452-28423-4"])
print(library)

print("-------5-------")

cities = {
    "New York": 8419000,
    "Los Angeles": 3980000,
    "Chicago": 2716000,
    "Houston": 2328000,
    "Phoenix": 1690000
}
highest_population = max(cities, key=lambda x : cities[x])
lowest_population = min(cities, key=lambda x : cities[x])

for k, v in cities.items():
    print(f"{k}'s population is {v}.")

print(f"{highest_population} has the highest population as {cities[highest_population]}.")
print(f"{lowest_population} has the lowest population as {cities[lowest_population]}.")

cities["Phoenix"] = 1700000
print(cities)

cities["San Francisco"] = 884000
print(cities)

print("-------6-------")

movies = {
    "Inception": {"year": 2010, "rating": 8.8, "genre": "Sci Fi"},
    "The Godfather": {"year": 1972, "rating": 9.2, "genre": "Crime"},
    "The Dark Knight": {"year": 2008, "rating": 9.0, "genre": "Action"},
    "Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "Crime"},
    "Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "Drama"}
}
# movies is dictionary.
highest_rating = max(movies, key=lambda x : movies[x]["rating"]) # it will show maximum key
for k, v in movies.items():
    print(f" The movie's name is \"{k}\", year :\"{movies[k]["year"]}\", rating : \"{movies[k]["rating"]}\", and genre is \"{movies[k]["genre"]}\"." )

print(f"{highest_rating} is the highest rating as {movies[highest_rating]["rating"]}.")

movies["The Matrix"] = {
    "year" : 1999,
    "rating" : 8.7,
    "genre" : "Sci Fi"
}
movies["Inception"]["rating"] = 9.0
print(movies)
del(movies["Pulp Fiction"])
print(movies)

print("-------7-------")

countries = {
"USA": "Washington, D.C.",
    "Canada": "Ottawa",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}
for k, v in countries.items():
    print(k, v)

print("".join([countries[x] for x in countries if x =="Germany"]))

countries["Australia"] = "Canberra"
print(countries)
countries["USA"] = "New Washington"
print(countries)
del(countries["France"])
print(countries)

print("-------8-------")

cart = [
    {"item": "apple", "quantity": 3, "price_per_unit": 0.5},
    {"item": "banana", "quantity": 6, "price_per_unit": 0.2},
    {"item": "orange", "quantity": 4, "price_per_unit": 0.3},
    {"item": "pear", "quantity": 2, "price_per_unit": 0.4} ]

Total_cost = sum(i["quantity"] * i["price_per_unit"] for i in cart)
for i in cart:
    for k,v in i.items():
        print(f"{k} is {v}", end=" ")
    print("")

print(f"The total cost of the cart is {Total_cost}")

cart.append({"item" : "grape", "quantity" : 5, "price_per_unit" : 0.6})

for x in cart:
    if x["item"] == "banana":
        x["quantity"] = 10
print(cart)

cart = [i for i in cart if i["item"] != "pear"]
print(cart)

print("-------9-------")

weather = {
    "Monday": {"temperature": 20, "humidity": 60},
    "Tuesday": {"temperature": 22, "humidity": 55},
    "Wednesday": {"temperature": 19, "humidity": 65},
    "Thursday": {"temperature": 23, "humidity": 50},
    "Friday": {"temperature": 21, "humidity": 70} }

highest_temp = max(weather, key=lambda x : weather[x]["temperature"])
lowest_hum = min(weather, key=lambda x : weather[x]["humidity"])

for k,v in weather.items():
    print(f"{k}'s ", end="")
    for v_k, v_v in v.items():
        print(f"{v_k} is {v_v}", end=" ")
    print()

print(f"The highest temperature is {weather[highest_temp]["temperature"]} and it is {highest_temp}.")
print(f"The lowest humidity is {weather[lowest_hum]["humidity"]} and it is {lowest_hum}.")

wed = weather["Wednesday"]
wed["temperature"] = 25
print(weather)

weather["Saturday"] = {
    "temperature" : 24,
    "humidity" : 60
}
print(weather)

print("-------10-------")

members = [
    {"name": "Alice", "age": 25, "books_borrowed": ["1984", "To Kill a Mockingbird"]},
    {"name": "Bob", "age": 30, "books_borrowed": ["The Catcher in the Rye"]},
    {"name": "Charlie", "age": 22, "books_borrowed": ["Brave New World", "1984"]},
    {"name": "David", "age": 35, "books_borrowed": ["The Great Gatsby"]} ]

borrowed = ""

for i in range(len(members)):
    for k,v in members[i].items():
        if k == "name" or k == "age":
            print(v, end=" ")
        if v == "Charlie":
            borrowed = members[i]["books_borrowed"]
    print()

print(f"Charlie borrowed {', '.join(borrowed)}.")

members.append({"name" : "Eve","age":28, "books_borrowed":["Pride and Prejudice"]})

for i in members:
    if i["name"] == "Bob":
        i["age"] = 31
print(members)

members = [ x for x in members if x["name"] != "David"]
print(members)