def roll_call_dwarves(names):
    for name in names:
        print(f"{names.index(name)+1}. {name}")

def summon_captain_planet(planeteer_calls):
   return [planetneer.capitalize() + "!" for planetneer in planeteer_calls]

def long_planeteer_calls(call_list):
    for call in call_list:
        if (len(call) > 4):
            return True
    return False

def find_the_cheese(list):
    cheeses = ["cheddar","gouda","camembert"]
    for item in list:
        if (item in cheeses):
            return item