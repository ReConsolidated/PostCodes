# modify path if necessary
fname = "PL.txt"
with open(fname, encoding="utf-8") as fin:
    data_str = fin.read()
# create a list of lists
data_list = []
for line in data_str.split('\n'):
    mylist = line.split('\t')
    if len(mylist) > 11:
        data_list.append(mylist)

# search zip code(s) by city and state

city = input("Podaj nazwę miasta: ")
for sublist in data_list:
    city_from_list = sublist[2]
    # shows all the zip codes for this location
    if city == city_from_list:
        zip_code = sublist[1]
        print("{} ma kod {}".format(city, zip_code))
