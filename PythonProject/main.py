import tkinter as tk
import tkinter.messagebox as messagebox

import HT_pakli



def eletkor():
    result = messagebox.askquestion("Kérdés", "Elmúlt 18 éves?")
    if result == "yes":
        return True
    else:
        return False

def mentes():

    vez= vezentry.get()
    ker= kerentry.get()
    with open('ma.txt', "w", encoding='utf-8') as fajl:
        sor = vez+" "+ker
        fajl.write(sor)


    try:
        vez = str(vez)
        ker= str(ker)
        root.destroy()
    except ValueError:
        messagebox.showerror("Hiba", "Helytelen adatot adott meg.")







root= tk.Tk()
root.geometry("300x300")
root.title("Adatok")
vezetekn=tk.Label(root,text="Vezetéknév",font=("Arial",15))
vezetekn.grid(row=2,column=0)
kereszn=tk.Label(root,text="Keresztnév",font=("Arial",15))
kereszn.grid(row=3,column=0)


vezentry= tk.Entry(root,width=15)
vezentry.grid(row=2,column=1)
kerentry= tk.Entry(root,width=15)
kerentry.grid(row=3,column=1)


keszgomb = tk.Button(root, text="Keszgomb", font=("Arial",15), command=mentes)
keszgomb.grid(row=5,column=1)

root.mainloop()

if(eletkor()==True):
    gepgyozelem = False

    jatekos = True
    oszto = False

    pakli = HT_pakli.HT_pakliakcio(jatekos, oszto)

    def kampec():
        ablak2.destroy()

    def beolvas_nev():
        try:
            with open("ma.txt", "r", encoding="utf-8") as fajl:
                adat = fajl.read().strip()
                nev.set(adat)
        except FileNotFoundError:
            nev.set("Nincs adat")

    def reset():

        takarit = pakli.torol()
        jhuzottlap.set(takarit)
        jatekosallas.set(takarit)
        mecsszitu.set(takarit)
        gephuzottlap.set(takarit)
        gepszam.set(takarit)





    def osztokor():

        oszto_info = pakli.osztojon()
        gephuzottlap.set(f"Húzott lap{oszto_info[2]}")
        gepszam.set(f"Osztó összege{oszto_info[1]}")

        if (gepgyozelem == True):
            mecsszitu.set("VESZTETTÉL")

        else:
            mecsszitu.set("GYŐZELEM")


    def HT_huzas():

        jatekos_info = pakli.gombhuzas()
        jhuzottlap.set(f"A szám amit utoljára húztál{jatekos_info[0]}")
        jatekosallas.set(f"Kártyáid összege:{jatekos_info[1]}")
        dontesseg = jatekos_info[2]
        if (dontesseg == 1):
            mecsszitu.set("VESZTETTÉL")
        elif (dontesseg == 2):
            mecsszitu.set("GYŐZELEM")

        return None


    ablak2 = tk.Tk()
    ablak2.geometry("750x600")
    ablak2.title("app")

    label1 = tk.Label(ablak2, text="Osztó", font=("Arial", 20)).place(x=375, y=0)

    jhuzottlap = tk.StringVar()
    jatekosallas = tk.StringVar()
    mecsszitu = tk.StringVar()
    gephuzottlap = tk.StringVar()
    gepszam = tk.StringVar()
    nev=tk.StringVar()
    beolvas_nev()
    label2 = tk.Label(ablak2, textvariable=gephuzottlap).place(x=200, y=60)
    label3 = tk.Label(ablak2, textvariable=gepszam).place(x=500, y=60)
    label4 = tk.Label(ablak2, textvariable=mecsszitu).place(x=375, y=120)
    label5 = tk.Label(ablak2, textvariable=jatekosallas).place(x=200, y=220)
    label6 = tk.Label(ablak2, textvariable=jhuzottlap).place(x=500, y=220)
    labelnev= tk.Label(ablak2, text="Játékos:").place(x=375, y=200)
    label7 = tk.Label(ablak2, textvariable=nev).place(x=375, y=220)


    button1 = tk.Button(ablak2, text="Huzok egy lapot", command=HT_huzas).place(x=200, y=320)
    button2 = tk.Button(ablak2, text="az oszto jön", command=osztokor).place(x=500, y=320)
    button3 = tk.Button(ablak2, text="Kiszállok",command= kampec, background="red").place(x=375, y=360)
    button4 = tk.Button(ablak2, text="Új játék", command=reset, background="green").place(x=375, y=500)

    ablak2.mainloop()



