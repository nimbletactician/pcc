alien = {'color':'green', 'point': 5}

# Direct Access of Element
print(alien['point'])

# Get()
print (alien.get('point'))

# Add a new key-value pair

alien['x-coordinate'] = 0
alien['y-coordinate'] = 25

print (alien)


# Map definition
fav_language = {
    "jen":"python",
    "sam":"go",
  "sara":"erlang",
    "tom": "c",
    "Mike": "c++"
}

# Loop entire Map
for k,v in fav_language.items() :
    print(f"\nKey: {k}")
    print(f"\nValue: {v}")

# Loop through keys
for name in fav_language:
    print(f"\vKey:{name}")

# get value
lookup_programmer = {'Mike','tom'}

for name in fav_language:
    if name in lookup_programmer:
        fav_lang = fav_language.get(name)
        print (fav_lang)

# loop over value

for language in sorted(set(fav_language.values())):
    print(language.title())