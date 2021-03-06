def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, transact):
    pet_shop["admin"]["total_cash"] += transact

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sales):
    pet_shop["admin"]["pets_sold"] += sales

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    return [pet for pet in pet_shop["pets"] if pet["breed"] == breed]
    # More longwinded way without using list comprehension:
    # of_breed = []
    # for pet in pet_shop["pets"]:
    #     if pet["breed"] == breed:
    #         of_breed.append(pet)
    # return of_breed

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, transact):
    customer["cash"] -= transact

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

# --- OPTIONAL ---

def customer_can_afford_pet(customer, pet):
    return customer["cash"] >= pet["price"]
# This is shorthand for the following, which also works:
    # if customer["cash"] >= pet["price"]:
    #     return True
    # else:
    #     return False

# This next one wasn't explicitly specified in the testing,
# but what it does is required for the next one.
# It would probably be equally valid to just put the contents into the
# next function directly, but I figured a more modular approach was better.
# The "find pet by name" function returns the pet rather than a boolean,
# and it has to return None for one of the tests to pass, so I couldn't
# use that on its own as a way of returning T/F here.
def is_pet_in_stock(pet_shop, pet):
    return pet in pet_shop["pets"]

def sell_pet_to_customer(pet_shop, pet, customer):
    if is_pet_in_stock(pet_shop, pet) and customer_can_afford_pet(customer, pet):
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        remove_pet_by_name(pet_shop, pet["name"])
        increase_pets_sold(pet_shop, 1)
        add_pet_to_customer(customer, pet)