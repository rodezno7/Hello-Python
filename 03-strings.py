name = "Bayron"
lastname = "Rodezno"
print(name)
print(lastname)

# Concatenar strings con el operador +
full_name = name + lastname
print(full_name)

full_name = name, lastname
print(full_name)

quote = "I'm Nicolas"
print(quote)

quote2 = 'She said "Hello" '
print(quote2)

# Format

template = "Hola, mi nombre es " + name + " y mi apellido es " + lastname
print(template)

template = f"Hola, my name is {name} and my lastname is {lastname}"
print(template)