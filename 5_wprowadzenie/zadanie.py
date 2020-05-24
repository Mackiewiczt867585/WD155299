class material:

    def __init__(self,r,x,y):
        self.rodzaj=r
        self.dlugosc=x
        self.szerokosc=y

    def wyswietl_nazwe(self):
        print(self.rodzaj)
        
class ubrania(material):
    
    def __init__(self,r,k,dk):
        self.rozmiar=r
        self.kolor=k
        self.dla_kogo=dk



class sweter(ubrania):

    def 