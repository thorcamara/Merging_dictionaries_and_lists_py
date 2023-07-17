crowd = list()
person = dict()
sum = average = 0
while True:
    person.clear()
    person['Name'] = str(input('Name: '))
    while True:
        person['Gender'] = str(input('Gender: [M/F] ')).upper()[0]
        if person['Gender'] in 'MF':
            break
        print('ERROR! Please, type only M or F.')
    person['Age'] = int(input('Age: '))
    sum += person['Age']
    crowd.append(person.copy())
    while True:
        answer = str(input('Do you want to continue? [\033[1;32mY\033[m/\033[1;31mN\033[m] ')).upper()[0]
        if answer in 'YN':
            break
        print('ERROR! Answer only Y or N.')
    if answer == 'N':
        break
print('-=' * 30)
print(f'A) In all we have \033[1;32m{len(crowd)}\033[m people registered.')
average = sum / len(crowd)
print(f'B) The average age is of \033[1;32m{average:5.2f}\033[m years.')
print(f'C) The womens registered were ', end='')
for p in crowd:
    if p['Gender'] in 'Ff':
        print(f'\033[1;32m{p["Name"]}\033[m ', end='')
print()
print('D) List of people that are above the average: ')
for p in crowd:
    if p['Age'] >= average:
        print(' ')
        for k, v in p.items():
            print(f'\033[1;32m{k} = {v}\033[m; ', end='')
        print()
print('\033[1;31m<< FINISHED >>\033[m')
