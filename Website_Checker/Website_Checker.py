import requests
from fake_useragent import user_agent
from http import HTTPStatus
import csv

class Webber:

    def get_websites(csv_path:str) ->list[str]:

        websites :list[str]=[]
        with open(csv_path) as file:
            reader = csv.reader
            print(type(reader))
            for row in reader:
                print(row)
                if "https://" not in row[1]:
                    websites.append(f"https://{row[1]}")
                else:
                    websites.append(row[1])
        return websites
    
    def get_user_agent() ->str:
        ua = user_agent
        return ua.chrome
    
    def get_user_description(status_code:str)->str:
        description:str = 
