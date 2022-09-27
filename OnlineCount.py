'''
This project is basically checking through a dictionary and finding the given value from the given key,
    implemented using the online check function
'''
def online_count(dic):
    count = 0
    people = []

    for i,j in dic.items():
        if j == 'online':
            count += 1
            people.append(i)

    return count



dic = statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
print(online_count(dic))