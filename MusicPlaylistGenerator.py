import random
Happy={}; Sad={}; Calming={}
my_list=[];new_list1=[]
Mood=[Happy,Sad,Calming]

H_1955_1970=['"Pyar Hua Ikrar Hua Hai Pyar Se" from Shree 420 (1955)',
                                    '"Mera Joota Hai Japani" from Shree 420 (1955)',
                                    '"Zara Saamne Toh Aao Chhaliye" from Janam Janam Ke Phere (1957)',
                                    '"Hai Apna Dil Toh Awara" from Solva Saal (1958)',
                                    '"Haal Kaisa Hai Janaab Ka Chalti Ka Naam Gaadi" from Chalti Ka Naam Gaadi (1959)',
                                    '"Sar Jo Tera Chakraye" from Pyaasa (1957)',
                                    '"Mera Joota Hai Japani" from Shree 420 (1955)']
H_1970_1999=['"Jai Jai Shiv Shankar" from Aap Ki Kasam (1974)',
                            '"Ina Mina Dika" from Amar Akbar Anthony (1977)',
                            '"Humko Tumse Ho Gaya Hai Pyar" from Amar Akbar Anthony (1977)',
                            '"Aap Jaisa Koi" from Qurbani (1980)',
                            '"Aaj Kal Tere Mere Pyaar Ke Charche" from Brahmachari (1968)',
                            '"Mere Khwabon Mein Jo Aaye" from Dilwale Dulhania Le Jayenge (1995)',
                            '"Om Shanti Om" from Karz (1980)',
                            '"Chaiyya Chaiyya" from Dil Se (1998)']
H_2000_2013=['"Kajra Re" from Bunty Aur Babli (2005)',
                                '"Desi Girl" from Dostana (2008)',
                                '"Om Shanti Om" from Om Shanti Om (2007)',
                                '"Mauja Hi Mauja" from Jab We Met (2007)',
                                '"Where’s The Party Tonight" from Kabhi Alvida Naa Kehna (2006)',
                                '"Senorita" from Zindagi Na Milegi Dobara (2011)',
                                '"Rock On!!" from Rock On!! (2008)',
                                '"Zoobi Doobi" from 3 Idiots (2009)',
                                '"Pee Loon" from Once Upon a Time in Mumbaai (2010)']
H_2014_2024=['"Sooraj Dooba Hain" from Roy (2015)',
            '"Matargashti" from Tamasha (2015)',
            '"Cutiepie" from Ae Dil Hai Mushkil (2016)',
            '"Ullu Ka Pattha" from Jagga Jasoos (2017)',
            '"Ban Ja Rani" from Tumhari Sulu (2017)',
            '"High Rated Gabru" from Nawabzaade (2018)',
            '"First Class" from Kalank (2019)',
            '"Slow Motion" from Bharat (2019)',
            '"Ghungroo" from War (2019)',
            '"Lehra Do" from 83 (2021)']

S_1955_1970=['"Jaane Woh Kaise Log The" from Pyaasa (1957)',
                '"Lag Jaa Gale" from Woh Kaun Thi? (1964)',
                '"Chitthi Na Koi Sandesh" from Dushman (1972)',                                    
                '"Dost Dost Na Raha" from Sangam (1964)',
                '"Kahin Deep Jale Kahin Dil" from Bees Saal Baad (1962)',
                '"Ae Mere Watan Ke Logo" (1963)',
                '"Aye Dil Mujhe Bata De" from Bhai Bhai (1956)']
S_1970_1999=['"Tere Bina Zindagi Se" from Aandhi (1975)',
                '"Tujhse Naraz Nahin Zindagi" from Masoom (1983)',
                '"Dil Dhoondta Hai" from Mausam (1975)',
                '"Kya Hua Tera Wada" from Hum Kisise Kum Naheen (1977)',
                '"Kahin Door Jab Din Dhal Jaye" from Anand (1971)', 
                '"Tadap Tadap Ke" from Hum Dil De Chuke Sanam (1999)',
                '"Ek Pyar Ka Nagma Hai" from Shor (1972)']
S_2000_2013=['"Dil De Diya Hai" from Masti (2004)',
            '"Tere Naam" from Tere Naam (2003)',
            '"Tere Bin" from Bas Ek Pal (2006)',
            '"Do Pal" from Veer-Zaara (2004)',
            '"Mitwa" from Kabhi Alvida Naa Kehna (2006)',
            '"Kal Ho Naa Ho" from Kal Ho Naa Ho (2003)',
            '"Tum Hi Ho" from Aashiqui 2 (2013)',
            '"Bepanah Pyaar Hai Aaja" from Krishna Cottage (2004)',
            '"Tere Liye" from Veer-Zaara (2004)']
S_2014_2024=['"Ae Dil Hai Mushkil" from Ae Dil Hai Mushkil (2016)',
            '"Tum Hi Ho" from Aashiqui 2 (2013)',
            '"Janam Janam" from Dilwale (2015)',
            '"Tera Ban Jaunga" from Kabir Singh (2019)',
            '"Kal Ho Naa Ho" from Kal Ho Naa Ho (2003)', 
            '"Raabta" from Agent Vinod (2012)', 
            '"Tum Hi Ho" from Aashiqui 2 (2013)', 
            '"Tum Hi Aana" from Marjaavaan (2019)']

C_1955_1970=['"Aaja Sanam Madhur Chandni Mein Hum" from Chori Chori (1956)'
            '"Chhod Do Aanchal Zamana Kya Kahega" from Paying Guest (1957)',
            '"Chhodo Kal Ki Baatein" from Hum Hindustani (1960)',
            '"Ae Meri Zohra Jabeen" from Waqt (1965)',
            '"Jahan Mein Jati Hoon" from Chori Chori (1956)',
            '"Ajeeb Dastan Hai Yeh" from Dil Apna Aur Preet Parai (1960)',
            '"Chaudhvin Ka Chand Ho" from Chaudhvin Ka Chand (1960)',
            '"Meri Jaan Mujhe Jaan Na Kaho" from Anubhav (1971)',
            '"Pyar Hua Ikrar Hua" from Shree 420 (1955)']   
C_1970_1999=['"Mere Sapno Ki Rani" from Aradhana (1969)',
            '"Chala Jata Hoon Kisi Ki Dhun Mein" from Mere Jeevan Saathi (1972)',
            '"Yeh Dosti" from Sholay (1975)',
            '"Yeh Shaam Mastani" from Kati Patang (1971)',
            '"Chala Jata Hoon" from Mere Jeevan Saathi (1972)',
            '"Dilbar Mere" from Satte Pe Satta (1982)',
            '"Mehbooba Mehbooba" from Sholay (1975)',
            '"Ek Ladki Ko Dekha" from 1942: A Love Story (1994)',
            '"Rimjhim Gire Saawan" from Manzil (1979)',
            '"Hum Tum Ek Kamre Mein" from Bobby (1973)',
            '"Pehla Nasha" from Jo Jeeta Wohi Sikandar (1992)']
C_2000_2013=['"Tera Hone Laga Hoon" from Ajab Prem Ki Ghazab Kahani (2009)',
            '"All Is Well" from 3 Idiots (2009)',
            '"Tumhi Ho Bandhu" from Cocktail (2012)',
            '"Jab Koi Baat Bigad Jaye" from Jurm (2005)',
            '"Pee Loon" from Once Upon a Time in Mumbaai (2010)',
            '"Agar Tum Mil Jao" from Zeher (2005)',
            '"Tum Mile" from Tum Mile (2009)']
C_2014_2024=['"Sau Aasmaan" from Baar Baar Dekho (2016)',
            '"Tera Ban Jaunga" from Kabir Singh (2019)',
            '"Sun Saathiya" from ABCD 2 (2015)',
            '"Samjhawan" from Humpty Sharma Ki Dulhania (2014)'
            '"Hasi Ban Gaye" from Hamari Adhuri Kahani (2015)',
            '"Raabta" from Raabta (2017)',
            '"Kaun Tujhe" from M.S. Dhoni: The Untold Story (2016)',
            '"Dil Diyan Gallan" from Tiger Zinda Hai (2017)',
            '"Tera Ban Jaunga" from Kabir Singh (2019)',
            '"Ve Maahi" from Kesari (2019)',
            '"Pal" from Jalebi (2018)']

Happy={
        "Black & White Era(1955-1970)":H_1955_1970,
        "90s Era(1970-1999)":H_1970_1999,
        "Era of 2000s(2000-2013)":H_2000_2013,
        "Golden Era(2014-2024)":H_2014_2024
    }
Sad={
        "Black & White Era(1955-1970)":S_1955_1970,
        "90s Era(1970-1999)":S_1970_1999,
        "Era of 2000s(2000-2013)":S_2000_2013,
        "Golden Era(2014-2024)":S_2014_2024
    }
Calming={
        "Black & White Era(1955-1970)":C_1955_1970,
        "90s Era(1970-1999)":C_1970_1999,
        "Era of 2000s(2000-2013)":C_2000_2013,
        "Golden Era(2014-2024)":C_2014_2024
}

def userChoice():    #Ask user's current mood and the type of songs they listen to 
   mood=input(f'''Welcome {name}! What's your mood today? 
                    Happy
                    Sad
                    Calming: ''').capitalize()
   print('''We have classified songs asaccording to era as -
            1.Black & White Era(1955-1970)
            2.90s Era(1970-1999)
            3.Era of 2000s(2000-2013)
            4.Golden Era(2014-2024)''')
   era=input('''
                Which one do you want to choose: 1,2,3 or 4
                Enter your choice: ''')
   lst=[mood,era]
   return lst 

#-----------------------> NEW FEATURE <--------------------------------
def generateRandomPlaylist(nm,m,e):  #Generate a playlist with randomly selected songs
    print(f"Hey {nm}! we have created a playlist according to your mood.")
    str1,str2='',''
    for x in range(0,5):
        if m=='Happy':
            if e==1:
                str1=random.choice(list(Happy['Black & White Era(1955-1970)']))
            elif e==2:
                str1=random.choice(list(Happy['90s Era(1970-1999)']))
            elif e==3:
                str1=random.choice(list(Happy['Era of 2000s(2000-2013)']))
            elif e==4:
                str1=random.choice(list(Happy['Golden Era(2014-2024)']))
        elif m=='Sad':
            if e==1:
                str1=random.choice(list(Sad['Black & White Era(1955-1970)']))
            elif e==2:
                str1=random.choice(list(Sad['90s Era(1970-1999)']))
            elif e==3:
                str1=random.choice(list(Sad['Era of 2000s(2000-2013)']))
            elif e==4:
                str1=random.choice(list(Sad['Golden Era(2014-2024)']))
        elif m=='Calming':
            if e==1:
                str1=random.choice(list(Calming['Black & White Era(1955-1970)']))
            elif e==2:
                str1=random.choice(list(Calming['90s Era(1970-1999)']))
            elif e==3:
                str1=random.choice(list(Calming['Era of 2000s(2000-2013)']))
            elif e==4:
                str1=random.choice(list(Calming['Golden Era(2014-2024)']))
        if str1!=str2:
            print(f"{x+1}.",str1)
            my_list.append(str1)
        str2=str1

def addMusic():      #Add N songs to the playlist ; N is user's choice
    num=int(input("Enter no. of songs you want to add: "))
    for i in range(0,num):
           music=input(f"Enter music no. {i+1}: ")
           my_list.append(music)
    return my_list
       
def editPlaylist():  #Shuffle or reverse the playlist
   new_list1.reverse()

name=input("Enter your name: ").capitalize()
choices=[]
choices=userChoice()
generateRandomPlaylist(nm=name,m=choices[0],e=int(choices[1]))
choice1=input("\nDo you want to add music to your playlist- Yes or No: ").capitalize()
if choice1=='Yes':
    new_list1=addMusic()
new_list1=my_list
choice2=input("Do you want to reverse your playlist- Yes or No: ").capitalize()
if choice2=='Yes':
    editPlaylist()
print("Now your list is ",new_list1)