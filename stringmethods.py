name = input("name: ")

# remove whitespace 
name = name.strip()

# makes only first letter upper case
name = name.capitalize()

# makes first letter of every word upper case
name = name.title()

# splitting into variables
first, last = name.split()