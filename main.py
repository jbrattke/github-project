import requests
import json

def main():
    response = requests.get("https://cat-fact.herokuapp.com/facts")
    data = response.json()
    print(data[0]['text'])

if __name__ == "__main__":
    main()