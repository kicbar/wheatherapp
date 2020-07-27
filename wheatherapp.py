from requests import get
from json import loads

def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)

    for row in loads(response.content):
        #print(row)
        #print(row['stacja'])
        if row['stacja'] == 'Warszawa':
            print(row)

if __name__ == '__main__':
    main()