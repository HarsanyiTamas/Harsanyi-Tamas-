import random

class HT_pakliakcio:
    def __init__(self,jatekh,gh):
        self.jatekoshuz=jatekh
        self.gephuz=gh
        self.jatekosossz=0
        self.gepossz=0


    def torol(self):
        self.gepossz=0
        self.jatekosossz=0
        tiszta= "..."
        return tiszta

    def huzas(self,a):

        packli = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        kartyahuz = random.choice(packli)
        osszeg= a+kartyahuz
        return kartyahuz, osszeg

    def gombhuzas(self):
            dontes=0
            eredmeny = self.huzas(self.jatekosossz)
            self.jatekosossz = eredmeny[1]
            if(self.jatekosossz>21):
                self.jatekoshuz = False
                dontes=1

            elif(self.jatekosossz==21):
                self.jatekoshuz = True
                dontes=2
            kiir= eredmeny[0]
            return (kiir, self.jatekosossz,dontes)

    def osztojon(self):
            sorsd= random.randint(1,1000)
            szamlalo=2

            for i in range(1,3):
                eredmeny = self.huzas(self.gepossz)
                self.gepossz = eredmeny[1]


            while(True):
                szamlalo=szamlalo+1
                if(self.gepossz>self.jatekosossz and self.gepossz<22):
                    gepgy = True
                    print(self.gepossz)
                    break


                elif(self.gepossz>21):
                    gepgy = False
                    print(self.gepossz)
                    break
                elif(self.gepossz<self.jatekosossz):
                    eredmeny = self.huzas(self.gepossz)
                    self.gepossz = eredmeny[1]
            else:
                pass

            return (gepgy, self.gepossz, szamlalo)






