list_of_abb_places = []
list_of_lga_places = []
with open('ABBNAME.txt') as f:
    for line in f.readlines():
        if(len(line)>2):
            list_of_abb_places.append(line.strip())

with open('LGANAME.txt') as f:
    for line in f.readlines():
        if(len(line)>2):
            list_of_lga_places.append(line.strip())

#print(str(len(list_of_abb_places)) + " : " + str(len(list_of_lga_places)))
difference = set(list_of_abb_places).difference(set(list_of_lga_places))
print(f'{len(difference)} "LGA"s not in our LGA Data:')
for item in difference:
    print(item)