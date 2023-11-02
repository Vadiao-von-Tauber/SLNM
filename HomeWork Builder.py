

class AlcoBoxBuilder:

    def __int__(self) -> None:
        self.sakkra = ''
        self.vodka = ''
        self.zbicien = ''
        self.rum = ''
        self.liquor = ''
        self.whisky = ''
        self.alco_set_box = []

    def add_sakkra(self, sakkra_name: str):
        self.sakkra = sakkra_name
        self.alco_set_box.append(self.sakkra)
        return self

    def add_vodka(self, vodka_name: str):
        self.vodka = vodka_name
        self.alco_set_box.append(self.vodka)
        return self

    def add_zbicien(self, zbicien_name: str):
        self.zbicien = zbicien_name
        self.alco_set_box.append(self.zbicien)
        return self

    def add_rum(self, rum_name:str):
        self.rum = rum_name
        self.alco_set_box.append(self.rum)
        return self

    def add_liquor(self, liquor_name: str):
        self.liquor = liquor_name
        self.alco_set_box.append(self.liquor)
        return self

    def add_whisky(self, whisky_name: str):
        self.whisky = whisky_name
        self.alco_set_box.append(self.whisky)
        return self

    def print_box(self) -> None:
        print('Alco Box:')
        for picky in self.alco_set_box:
            print('\t' + picky)

if __name__ == '__main__':

     AlcoBoxBuilder()\
           .add_sakkra()\
           .add_vodka()\
           .add_zbicien()\
           .add_liquor()\
           .add_rum()\
           .add_whisky()\
           .print_box()
