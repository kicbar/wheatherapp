from requests import get
from json import loads

#set city for get data 
CITIES = 'Warszawa'

def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)

    for row in loads(response.content):
        if row['stacja'] in CITIES:
            print(row)

if __name__ == '__main__':
    print('Hello in wheatherApp.')
    main()