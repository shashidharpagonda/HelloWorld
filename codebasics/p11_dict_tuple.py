'''
We have following information on countries and their population (population is in crores),
    Country	Population
    China	143
    India	136
    USA	32
    Pakistan	21
'''
'''
1. Using above create a dictionary of countries and its population
'''
'''
2. Write a program that asks user for three type of inputs,
    2.1. print: if user enter print then it should print all countries with their population in this format,
        china==>143
        india==>136
        usa==>32
        pakistan==>21
'''
'''
    2.2 add: if user input add then it should further ask for a country name to add.
             If country already exist in our dataset then it should print that it exist and do nothing.
             If it doesn't then it asks for population and add that new country/population in our dictionary and
             print it
'''
'''
    2.3 remove: when user inputs remove it should ask for a country to remove.
                If country exist in our dictionary then remove it and
                    print new dictionary using format shown above in (a).
                Else print that country doesn't exist!
'''
'''
    2.4 query: on this again ask user for which country he or she wants to query.
                When user inputs that country it will print population of that country.
'''
population={'China':143,'India':136,'USA':32,'Pakistan':21} #dictonary
def add():
    country=input('Enter the country:')
    if country in population:
        print(f'{country}==>{population.get(country)}')
        return
    p=input(f'Enter the population of {country}:')
    population[country]=int(p) #Add new entry in dict
    print(f'{country}==>{population.get(country)} is added in our s/m')
    print_all()

def remove():
    country=input('Enter the country to remove:')
    if country not in population:
        print('country doesnt exist')
        return
    del population[country]
    print_all()


def query():
    country=input('which country name to query :')
    country=country.lower()
    if country not in population:
        print("country doesn't exist in our database. Terminating")
        return
    print(f'Population of country {country}==>{population.get(country)}')


def print_all():
    for key,val in population.items():
        print(f'{key}==>{val}')

def main():
    op=input("Enter operation (add, remove, query or print):")
    if op.lower()=='add':
        add()
    elif op.lower()=='remove':
        remove()
    elif op.lower()=='query':
        query()
    elif op.lower()=='print':
        print_all()

if __name__=='__main__':
    main()