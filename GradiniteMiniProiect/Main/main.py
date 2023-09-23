from GradiniteMiniProiect.ClaseGradinita.GradinitaPrivata import GradinitaPrivata
from GradiniteMiniProiect.ClaseGradinita.GradinitaPublica import GradinitaPublica
from GradiniteMiniProiect.ClaseGradinita.GradinitaPublica25 import GradinitaPublica25

if __name__ == '__main__':    # inainte de aceasta sintaxa definim/importam
    gradinita_privata1 = GradinitaPrivata()
    gradinita_privata1.activitate_practica()
    gradinita_privata1.ora_de_somn()

    # aici incepem sa cream un obiect pentru clasa GradinitaPublica
    '''liniile 11 si 12 rezulta din faptul ca am apelat functiile clasei GradinitaPublica prin obiectul
    clase, gradinita_publica1'''

    gradinita_publica1 = GradinitaPublica()
    gradinita_publica1.activitate_practica()
    gradinita_publica1.ora_de_somn()

    # aici am creat obiect pentru clasa GradinitaPublica25
    # pe linia 21 am aplelat functia clasei GradinitaPublica25

    gradinita_publica25 = GradinitaPublica25()
    gradinita_publica25.activitate_practica()

    gradinita_publica25.calcul_buline_rosii()

    #apelam metoda introduceti_informatii_elevi pe obiectul GradinitaPublica25
    gradinita_publica25.introduceti_informatii_elevi()
