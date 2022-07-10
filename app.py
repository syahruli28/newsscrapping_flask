from flask import Flask, flash, render_template, request
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

# route untuk ta saya : newsscraper
@app.route('/', methods=["POST", "GET"])
def index():

    # tampilkan bila tombol greet ditekan
    if request.method == 'POST':
        flash("Proses scrapping selesai, masukan data untuk scrapping kembali." ) # tampilkan pesan flash

        # mulai proses scrapping
        key = request.form['name']

        url = [
            'https://www.detik.com/search/searchall?query={}&siteid=2'.format(key),
            'https://search.kompas.com/search/?q={}&submit=Kirim'.format(key),
            'https://search.kapanlagi.com/?q={}'.format(key),
            'https://www.tribunnews.com/search?q={}&cx=partner-pub-7486139053367666%3A4965051114&cof=FORID%3A10&ie=UTF-8&siteurl=www.tribunnews.com'.format(key) #,
            # 'https://www.tempo.co/search?q={}#gsc.tab=0&gsc.q={}&gsc.sort='.format(key, key)
            ]

        for u in url:
            driver = webdriver.Chrome("chromedriver.exe")
            driver.get(u)
            content = driver.page_source
            driver.quit()
            soup = BeautifulSoup(content, 'html.parser')

            # persiapan membuat file csv dan menambahkan headernya
            f = csv.writer(open('hasil.csv', 'w', newline='\n'))
            header = ['News Portal', 'Pencarian Terkait', 'Judul', 'Waktu Post & Rangkuman']
            f.writerow(header)

            # melakukan perulangan pada array url
            if 'detik.com' in u:
                # DETIK.COM
                # variabel tambahan
                portaldetik = 'Detik.com'
                keysearchdetik = key
                # list
                turun = soup.findAll('span', attrs={'class':'box_text'})
                samping = soup.findAll('div', attrs={'class':'box_text text_inside'})
                # data yang akan di crawl
                detikrawtitle = soup.findAll('h2', attrs={'class':'title'})
                detikrawrangkuman = soup.findAll('p')
                detikrawdate = soup.findAll('span', attrs={'class':'date'})

                detik_tambah_satu = open('hasil.csv', 'a', newline='\n')
                # loop
                for x in range(0, len(turun)):
                    portal = portaldetik
                    search = keysearchdetik
                    title = ("{}".format(detikrawtitle[x].text.strip()))
                    rrangkuman = ("{}".format(detikrawrangkuman[x].text.strip()))  
                    date = ("{}".format(detikrawdate[x].text.strip()))
                    rangkuman = date + ", Rangkuman berita : " + rrangkuman  
                    # menulis ke file csv
                    detik_save_pertama = csv.writer(detik_tambah_satu)
                    detik_save_pertama.writerow([portal, search, title, rangkuman])

                detik_tambah_dua = open('hasil.csv', 'a', newline='\n')
                for x in range(0, len(samping)):
                    portal = portaldetik
                    search = keysearchdetik
                    title = ("{}".format(samping[x].text.strip()))
                    rangkuman = 'Tidak ada'
                    # date = 'Tidak dicantumkam'
                    # menulis ke file csv
                    detik_save_kedua = csv.writer(detik_tambah_dua)
                    detik_save_kedua.writerow([portal, search, title, rangkuman])

            elif 'kompas.com' in u:
                # KOMPAS.COM
                # variabel tambahan
                portalkompas = 'Kompas.com'
                keysearchkompas = key
                # list
                kompasloop = soup.findAll('div', attrs={'class':'gsc-webResult gsc-result'})
                # data yang akan di crawl
                kompasrawtitle = soup.findAll('a', attrs={'class':'gs-title'})
                kompasrawrangkuman = soup.findAll('div', attrs={'class':'gs-bidi-start-align gs-snippet'})

                kompas_tambah_satu = open('hasil.csv', 'a', newline='\n')
                # loop
                for x in range(0, len(kompasloop)):
                    portal = portalkompas
                    search = keysearchkompas
                    title = ("{}".format(kompasrawtitle[x].text.strip()))
                    rangkuman = ("{}".format(kompasrawrangkuman[x].text.strip()))  
                    # date = 'Tidak dicantumkan'  
                    # menulis ke file csv
                    kompas_save_pertama = csv.writer(kompas_tambah_satu)
                    kompas_save_pertama.writerow([portal, search, title, rangkuman])

            elif 'kapanlagi.com' in u:
                # KAPANLAGI.COM
                # variabel tambahan
                portalkl = 'KapanLagi.com'
                keysearchkl = key
                # list
                klloop = soup.findAll('div', attrs={'class':'gsc-webResult gsc-result'})
                # data yang akan di crawl
                klrawtitle = soup.findAll('a', attrs={'class':'gs-title'})
                klrawrangkuman = soup.findAll('div', attrs={'class':'gs-bidi-start-align gs-snippet'})

                kl_tambah_satu = open('hasil.csv', 'a', newline='\n')
                # loop
                for x in range(0, len(klloop)):
                    portal = portalkl
                    search = keysearchkl
                    title = ("{}".format(klrawtitle[x].text.strip()))
                    rangkuman = ("{}".format(klrawrangkuman[x].text.strip()))  
                    # date = 'Tidak dicantumkan'  
                    # menulis ke file csv
                    kl_save_pertama = csv.writer(kl_tambah_satu)
                    kl_save_pertama.writerow([portal, search, title, rangkuman])

            elif 'tribunnews.com' in u:
                # TRIBUNNEWS.COM
                # variabel tambahan
                portaltribun = 'Tribunnews.com'
                keysearchtribun = key
                # list
                tribunloop = soup.findAll('div', attrs={'class':'gsc-webResult gsc-result'})
                # data yang akan di crawl
                tribunrawtitle = soup.findAll('a', attrs={'class':'gs-title'})
                tribunrawrangkuman = soup.findAll('div', attrs={'class':'gs-bidi-start-align gs-snippet'})

                tribun_tambah_satu = open('hasil.csv', 'a', newline='\n')
                # loop
                for x in range(0, len(tribunloop)):
                    portal = portaltribun
                    search = keysearchtribun
                    title = ("{}".format(tribunrawtitle[x].text.strip()))
                    rangkuman = ("{}".format(tribunrawrangkuman[x].text.strip()))  
                    # date = 'Tidak dicantumkan'  
                    # menulis ke file csv
                    tribun_save_pertama = csv.writer(tribun_tambah_satu)
                    tribun_save_pertama.writerow([portal, search, title, rangkuman])


        # akhir proses scrapping
        return render_template('newsscraper.html') # kembali ke halaman awal

    # jika belum ada tombol ditekan
    flash("Silahkan masukan keyword pencarian.")
    return render_template('newsscraper.html') # kembali ke halaman awal