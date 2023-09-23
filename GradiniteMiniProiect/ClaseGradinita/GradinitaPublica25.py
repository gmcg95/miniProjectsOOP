from GradiniteMiniProiect.ClaseGradinita.GradinitaPublica import GradinitaPublica
from GradiniteMiniProiect.ClaseGradinita.PrintColorString import PrintColorString

class GradinitaPublica25(GradinitaPublica):
    def activitate_practica(self):
        print('Copiii se joaca in curte pe balansoar')

    def calcul_buline_rosii(self):
        suma_buline = 0
        nr_elevi = int(input('Introduceti numarul de elevi:\n'))
        for elev in range(1, nr_elevi+1):  #for each;pentru fiecare elev se executa comanda de mai jos
            nr_buline = int(input(f'Introduceti numarul de buline rosii pentru copilul {elev}:\n'))
            suma_buline += nr_buline
        media_artimetica_buline = suma_buline / nr_elevi
        print(f'Media bulinelor este {media_artimetica_buline}:\n')
        if media_artimetica_buline > 5:
            print(f'{PrintColorString.RED} Elevii acestei gradinite sunt foarte neastamparati{PrintColorString.RESET}')
'''am apelat metoda clasei PrintColorString. La inceput s-a pus culoarea(declarata ca atribut in acea clasa,
iar la final am dat reset, pentru a nu ramane mereu rosu '''



elev1 : {
    'nume' : 'Matei',
    'nume_parinti' : 'Ion si Maria',
    'varsa_elev' : 9,
    'activitate_preferata' : 'colorat'
    }


    def introduceti_informatii_elevi(self):
        info = eval(input('Introduceti datele despre elevi:\n'))
        #eval preia input-uri si le uneste
        for elev_cheie, detalii_value in info.items():
            print(f'Elevul numarul {elev_cheie}')
            for date_cheie, date_value in detalii_value.items():
                print(f'{date_cheie} : {date_cheie}')


