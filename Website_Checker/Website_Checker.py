import requests
from fake_useragent import UserAgent
from http import HTTPStatus
import csv
import os
real_path:str = os.path.dirname(os.path.realpath(__file__))

class Webber:

    def get_websites(self,csv_path:str) ->list[str]:

        websites :list[str]=[]
        with open(f'{real_path}/{csv_path}', 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                if "https://" not in row[1]:
                    websites.append(f"https://{row[1]}")
                else:
                    websites.append(row[1])
        return websites
    
    def get_user_agent(self) ->str:
        ua = UserAgent()
        return ua.chrome
    
    def get_user_description(self,status_code:int)->str:
        for value in HTTPStatus:
            if value == status_code:
                description: str = f'({value} {value.name}) {value.description}'
                return description
        return '??? NOT FOUND'

    def check_website(self,website:str,user_agent):
        try:
            code:int = requests.get(website,headers={"User-Agent":user_agent}).status_code
            print(self.get_user_description(code),website)
        except Exception as e:
            print(f"Could not find any information {website}")

    def main(self):
        sites: list[str] = self.get_websites('websites.csv')
        user_agent:str=self.get_user_agent()

        for site in sites:
            self.check_website(site,user_agent)

user = Webber()            
if __name__ == '__main__':
    user.main()