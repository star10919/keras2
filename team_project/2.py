import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

class Nutrition(object):
    # url = 'https://terms.naver.com/list.naver?cid=59320&categoryId=59320'
    url = None
    driver_path = 'c:/Program Files/Google/Chrome/chromedriver'
    dict = {}
    df = None
    food_name = []
    food_nut = []
    new_food_nut = []
    new_food_gram = []
    new_food_kcal = []
    one_nut = []
    

    def scrap_name(self):

        for i in range(1):
            self.url = f'https://terms.naver.com/list.naver?cid=59320&categoryId=59320&page={i}'
            driver = webdriver.Chrome(self.driver_path)
            driver.get(self.url)
            all_div = BeautifulSoup(driver.page_source, 'html.parser')
            ls1 = all_div.find_all("div", {"class": "subject"})     # name
            for i in ls1:
                self.food_name.append(i.find('a').text)
            # print(self.food_name)

            ls2 = all_div.find_all("p", {"class": "desc __ellipsis"})      # nutrition
            for i in ls2:
                self.food_nut.append(i.text)          
            # print(self.food_nut)

            ls3 = all_div.find_all("span", {"class": "info"})        # 1회 제공량
            for i in ls3:
                self.one_nut.append(i.text)
            # print(self.one_nut)
                

            # print(len(self.food_name))  # 16
            # print(len(self.food_nut))   # 15
            self.food_name.remove('인문과학')     # 불필요한 요소 제거
            # print(len(self.food_name))  # 15
            for i in self.food_nut:
                temp = i.replace('\n', '').replace('\t', '').replace(' ', '').replace('[영양성분]', '')     # 불필요한 요소 제거
                self.new_food_nut.append(temp)
            
            for word in self.one_nut:
                if '1회제공량' in word:
                    self.one_nut.append(word)
                elif '칼로리' in word:
                    self.one_nut.append(word)
                else:
                    self.one_nut.remove
            print(self.one_nut)

            

            for i, j in enumerate(self.food_name):
                # print('i,j :\n',i, j)
                # print('name :\n',self.food_name[i])
                # print('nutrition :\n',self.food_nut[i])
                self.dict[self.food_name[i]] = [self.new_food_nut[i], self.one_nut[word]]
            
            driver.close()

        print(self.dict)
        


    '''
        for i in ls:
            print()
            self.food_nut.append(i.find("p").text)
        driver.close()
    def insert_dict(self):
        for i, j in zip(self.food_name, self.food_nut):
            self.dict[i] = j
            print(f'{i}:{j}')
    def dict_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(dt, orient='index')
        print(self.df)
    def df_to_csv(self):
        path = './data/food_nutrition.csv'
        self.df.to_csv(path, sep=',', na_rep='Nan')
    '''
    @staticmethod
    def main():
        nut = Nutrition()
        nut.scrap_name()

Nutrition.main()