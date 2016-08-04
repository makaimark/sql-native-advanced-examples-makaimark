import random
import csv

first_name_values =['Miklós', 'Tamás', 'Dániel', 'Mateusz', 'Attila',
                    'Pál', 'Sándor', 'Prezmek', 'John', 'Tim',
                    'Matthew', 'Andy', 'Giancarlo']

last_name_values = ['Beöthy', 'Tompa', 'Salamon', 'Ostafil', 'Molnár',
                    'Monoczki', 'Szodoray', 'Ciacka', 'Carrey', 'Obama',
                    'Lebron', 'Hamilton', 'Fisichella']

birthday = random.randint(1960,1995)

email = random.choice(first_name_values) + '@codecool.com'

city_values = ['Budapest', 'Miskolc', 'Krakow', 'Barcelona', 'New York']

# phone_number = '+' + random.randint(1000000000,9999999999)

level = random.randint(1,10)

with open('fake_mentor_candidates.csv', 'w') as mycsvfile:
    csvwriter = csv.writer(mycsvfile, delimiter=',')
    row = []
    for i in range(10000):
        row.append(random.choice(first_name_values))
        row.append(random.choice(last_name_values))
        row.append('+' + str(random.randint(1000000000,9999999999)))
        row.append(random.choice(first_name_values) + '@codecool.com')
        row.append(random.choice(city_values))
        row.append(random.randint(1,10))
        row.append(random.randint(1960,1995))
        csvwriter.writerow(row)
        row = []