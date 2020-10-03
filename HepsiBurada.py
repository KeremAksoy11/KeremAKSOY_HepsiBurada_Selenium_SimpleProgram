from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
from faker import Faker


tekrar_sayisi = int(input("Kaç Kere Hesap Açılsın: "))
kaç_kere = 1
while  True:
    kaç_kere = kaç_kere + 1
    fake = Faker('tr_TR')
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = first_name + last_name + "646546" + "@hotmail.com"
    Sifre = "BarryAllenCoder11"
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = "https://giris.hepsiburada.com/?ReturnUrl=https%3A%2F%2Foauth.hepsiburada.com%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3DSPA%26redirect_uri%3Dhttps%253A%252F%252Fwww.hepsiburada.com%252Fuyelik%252Fcallback%26response_type%3Dcode%26scope%3Dopenid%2520profile%26state%3D4e7cc96d88a54b799a239e93058e93e5%26code_challenge%3DqP1e_zpbLFaicgay2ya4BvC3r1-CMZPTvCHNwtZwhcE%26code_challenge_method%3DS256%26response_mode%3Dquery"
    driver.get(url)


    UyeOl =driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]')
    UyeOl.click()
    time.sleep(2)



    ad = driver.find_element_by_name("firstName")
    time.sleep(1)
    ad.send_keys(first_name)
    time.sleep(1)


    SoyAd = driver.find_element_by_name("lastName")
    time.sleep(1)
    SoyAd.send_keys(last_name)
    time.sleep(1)



    Email = driver.find_element_by_name("email")
    time.sleep(1)
    Email.send_keys(email)
    time.sleep(1)


    Password = driver.find_element_by_name("password")
    time.sleep(1)
    Password.send_keys(Sifre)
    time.sleep(1)

    sozlesme = driver.find_element_by_xpath("//*[@id='checkSubscribeEmail']")
    sozlesme.click()
    time.sleep(1)

    KabulEt =driver.find_element_by_xpath("//*[@id='btnSignUpSubmit']")
    KabulEt.click()
    time.sleep(2)

    with open("HepsiBuradaVeri.txt","a+",encoding="utf-8") as file:
        file.write("\nAD: {}\nSOYAD: {}\nEmail: {}\nŞİFRE: {}\n".format(first_name,last_name,email,Sifre))


    time.sleep(3)
    driver.close()
    
    if kaç_kere > tekrar_sayisi:
        print("İşlem Başarıyla Gerçekleşti. Program 3 Saniye Sonra Kapanacaktır.")
        time.sleep(3)
        break

print("Açılan Hesapların Bilgileri Aşağıda Yer Almaktadır.HepsiBuradaVeri Adlı Dosyamızdan da Verilere Ulaşabilirsiniz.")


for dosya_okuma in open('HepsiBuradaVeri.txt', 'r',encoding="utf-8"):  
    print(dosya_okuma)  


    
    