try:
    import requests,re,sys,time
    from bs4 import BeautifulSoup
except:
    print("Bazı modüller yüklü değil.")



if __name__ == "__main__":
    print("\n\nKullanımı : python deneme.py [URL]\n\n")




#   URL PARCALAMA İSLEMİ
url = sys.argv[1]
url_split = url.split("://")
url_argv_2 = url_split[1]



# URL İSTEK VE KAYNAK KODLARI
r = requests.get(url)
status = r.status_code
r_kaynak = r.content
r_kaynak_split = r_kaynak.split()
soup = BeautifulSoup(r_kaynak,"lxml")



#    URL İCERİSİNDEKİ BÜTÜN LİNKLERİ GOSTERİR
def butunlinkler():
    for i in r_kaynak_split:
        sonuc = re.search("http://",str(i))
        sonuc2 = re.search("https://", str(i))
        if sonuc:
            print("[*] "+sonuc.string,"\n")
        if sonuc2:
            print("[*] ",sonuc2.string,"\n")
        else:
            continue

butunlinkler()


"""
#   URL İCERİSİNDE SADECE O SİTENİN DOMAİNİNE AİT SİTELERİ GOSTERİR
def sitelink():
    for i in r_kaynak_split:
        sonuc = re.search("http://"+str(url_argv_2),str(i))
        sonuc2 = re.search("https://"+str(url_argv_2), str(i))
        if sonuc:
            print("[*] "+sonuc.string,"\n")
        if sonuc2:
            print("[*] ",sonuc2.string,"\n")
        else:
            continue
    print("#    Bulunan Sonuçlar   #\r\n")
"""


"""

#   SECİM AŞAMASI
print("Hoşgeldiniz\r\nLütfen secim yapınız.")
print("""


""","\n")
secim = input("Secim :")
if secim == "1":
    butunlinkler()
if secim == "2":
    sitelink()

"""









