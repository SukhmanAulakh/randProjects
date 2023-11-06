import requests
import json
import re
 
def compare_strings(string1, string2):
    pattern = re.compile(string2)
    match = re.search(pattern, string1)

response = requests.get('https://api.imgflip.com/get_memes')

memename = input("What meme you want?:")


found = False
for data in response.json()['data']['memes']:

    if memename.upper() in data['name'].upper():
        print(data['url'],"\n")
        found = True

if found == False:
    print("No memes of that name exist:")
    morememe = input("Do you want to see the name list of all memes possible?: yes or no")
    if int(morememe) == 1:
        for data in response.json()['data']['memes']:
            print(data['name'],"\n")
    else:
        print("Have a good day!")

