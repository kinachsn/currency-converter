https://github.com/kinachsn/CurrencyConverter.git
import requests
import json
class exchange:
    def __init__(self,döviz1,döviz2,miktar):
        self.döviz1 = döviz1
        self.döviz2 = döviz2
        self.miktar = miktar
    def convert(self):
        url = f'https://api.exchangerate.host/latest?base={self.döviz1}'
        response = requests.get(url)
        data = json.loads(response.text)
        # güncel borsa görüntülemek istersem
        # print(data)
        # print(type(data))
        result=float(data['rates'][self.döviz2])*float(self.miktar)
        print(f"1 {self.döviz1} = {data['rates'][self.döviz2]} {self.döviz2}")
        print(f"{self.miktar} {self.döviz1} = {result} {self.döviz2}")
            
while True:
    x=int(input("1- Döviz Bozdurma\n2- Çıkış\nYapmak istediğiniz işlemi giriniz: "))
    if x == 1:
        print('$'*50)
        print("  Welcome to exchange Currency Converter  ".center(50,'$'))
        print('$'*50)
        print("Örneğin; USD,TRY,EUR...")
        döviz1 = input("Bozdurmak istediğiniz Döviz türü: ").upper()
        döviz2 = input("Almak istediğiniz Döviz türü: ").upper()
        miktar = input("Bozdurmak istediğiniz miktar: ")
        döviz = exchange(döviz1, döviz2,miktar)
        döviz.convert()
    elif x == 2:
        print("Çıkış yapıldı. Yine bekleriz...\nHasanKNC®")
        break