spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [i["name"] for i in spicy_foods ]


def get_spiciest_foods(spicy_foods):
    return [i for i in spicy_foods if i["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    name = "name"
    cuisine = "cuisine"
    heat_level = "heat_level"
    spice = "🌶"
    for i in spicy_foods:
        print (f"{i[name]} ({i[cuisine]}) | Heat Level: {spice * i[heat_level]}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for i in spicy_foods:
        if i["cuisine"] == cuisine:
            return i

def print_spiciest_foods(spicy_foods):
    name = "name"
    cuisine = "cuisine"
    heat_level = "heat_level"
    spice = "🌶"
    for i in spicy_foods:
        if i["heat_level"] > 5:
            print (f"{i[name]} ({i[cuisine]}) | Heat Level: {spice * i[heat_level]}")
    

def get_average_heat_level(spicy_foods):
    sum = 0
    for i in spicy_foods:
        sum = sum + i["heat_level"]
    
    return sum/len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    

create_spicy_food(spicy_foods, {
     'name': 'Griot',
     'cuisine': 'Haitian',
     'heat_level': 10,
})

print (spicy_foods)