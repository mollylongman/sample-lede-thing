"Molly Longman"
"June 6, 2023" 
"Homework 1"

birth_year = input("what year were you born?")
birth_year = int(birth_year)
age = 2023 - birth_year
print(age)
heartbeat = 35000000 * age
print(heartbeat)
whale_heartbeat = 2 * 60 * 24 * 365 * age
print(f"the whale's heart beat is", whale_heartbeat)
rabbit_heartbeat = round((140 * 60 * 24 * 365 * age)/1000000)
print(f"the rabbit's heart has beaten {rabbit_heartbeat} million times in my life")
venus_years = age / .615
print(f"The person is {venus_years} on Venus")
neptune_years = age / 165
print(f"the user is {neptune_years} on Neptune")
if 1994 > birth_year:
    print("the user is older than me")
elif 1994 == birth_year:
    print("The user is the same age as me")
else:
    print("the user is younger than me") 
#else:
    #print("dude I have no idea how old this user is compared to me!")
