import random

H_1955_1970 = [
    '"Pyar Hua Ikrar Hua Hai Pyar Se" from Shree 420 (1955)',
    '"Mera Joota Hai Japani" from Shree 420 (1955)',
    '"Zara Saamne Toh Aao Chhaliye" from Janam Janam Ke Phere (1957)',
    '"Hai Apna Dil Toh Awara" from Solva Saal (1958)',
    '"Haal Kaisa Hai Janaab Ka Chalti Ka Naam Gaadi" from Chalti Ka Naam Gaadi (1959)',
    '"Sar Jo Tera Chakraye" from Pyaasa (1957)',
    '"Eena Meena Deeka" from Aasha (1957)'
]

H_1970_1999 = [
    '"Jai Jai Shiv Shankar" from Aap Ki Kasam (1974)',
    '"Ina Mina Dika" from Amar Akbar Anthony (1977)',
    '"Humko Tumse Ho Gaya Hai Pyar" from Amar Akbar Anthony (1977)',
    '"Aap Jaisa Koi" from Qurbani (1980)',
    '"Mere Khwabon Mein Jo Aaye" from Dilwale Dulhania Le Jayenge (1995)',
    '"Om Shanti Om" from Karz (1980)',
    '"Chaiyya Chaiyya" from Dil Se (1998)',
    '"Yeh Shaam Mastani" from Kati Patang (1971)'
]

H_2000_2013 = [
    '"Kajra Re" from Bunty Aur Babli (2005)',
    '"Desi Girl" from Dostana (2008)',
    '"Om Shanti Om" from Om Shanti Om (2007)',
    '"Mauja Hi Mauja" from Jab We Met (2007)',
    '"Where’s The Party Tonight" from Kabhi Alvida Naa Kehna (2006)',
    '"Senorita" from Zindagi Na Milegi Dobara (2011)',
    '"Rock On!!" from Rock On!! (2008)',
    '"Zoobi Doobi" from 3 Idiots (2009)',
    '"Pee Loon" from Once Upon a Time in Mumbaai (2010)'
]

H_2014_2024 = [
    '"Sooraj Dooba Hain" from Roy (2015)',
    '"Matargashti" from Tamasha (2015)',
    '"Cutiepie" from Ae Dil Hai Mushkil (2016)',
    '"Ullu Ka Pattha" from Jagga Jasoos (2017)',
    '"Ban Ja Rani" from Tumhari Sulu (2017)',
    '"High Rated Gabru" from Nawabzaade (2018)',
    '"First Class" from Kalank (2019)',
    '"Slow Motion" from Bharat (2019)',
    '"Ghungroo" from War (2019)',
    '"Lehra Do" from 83 (2021)'
]

S_1955_1970 = [
    '"Jaane Woh Kaise Log The" from Pyaasa (1957)',
    '"Lag Jaa Gale" from Woh Kaun Thi? (1964)',
    '"Waqt Ne Kiya Kya Haseen Sitam" from Kaagaz Ke Phool (1959)',
    '"Dost Dost Na Raha" from Sangam (1964)',
    '"Kahin Deep Jale Kahin Dil" from Bees Saal Baad (1962)',
    '"Ae Mere Watan Ke Logo" (1963)',
    '"Aye Dil Mujhe Bata De" from Bhai Bhai (1956)'
]

S_1970_1999 = [
    '"Tere Bina Zindagi Se" from Aandhi (1975)',
    '"Tujhse Naraz Nahin Zindagi" from Masoom (1983)',
    '"Dil Dhoondta Hai" from Mausam (1975)',
    '"Kya Hua Tera Wada" from Hum Kisise Kum Naheen (1977)',
    '"Kahin Door Jab Din Dhal Jaye" from Anand (1971)',
    '"Tadap Tadap Ke" from Hum Dil De Chuke Sanam (1999)',
    '"Ek Pyar Ka Nagma Hai" from Shor (1972)'
]

S_2000_2013 = [
    '"Dil De Diya Hai" from Masti (2004)',
    '"Tere Naam" from Tere Naam (2003)',
    '"Tere Bin" from Bas Ek Pal (2006)',
    '"Do Pal" from Veer-Zaara (2004)',
    '"Mitwa" from Kabhi Alvida Naa Kehna (2006)',
    '"Kal Ho Naa Ho" from Kal Ho Naa Ho (2003)',
    '"Tum Hi Ho" from Aashiqui 2 (2013)',
    '"Bepanah Pyaar Hai Aaja" from Krishna Cottage (2004)',
    '"Tere Liye" from Veer-Zaara (2004)'
]

S_2014_2024 = [
    '"Ae Dil Hai Mushkil" from Ae Dil Hai Mushkil (2016)',
    '"Channa Mereya" from Ae Dil Hai Mushkil (2016)',
    '"Janam Janam" from Dilwale (2015)',
    '"Hamari Adhuri Kahani" from Hamari Adhuri Kahani (2015)',
    '"Bekhayali" from Kabir Singh (2019)',
    '"Main Dhoondne Ko Zamaane Mein" from Heartless (2014)',
    '"Tum Hi Aana" from Marjaavaan (2019)'
]

C_1955_1970 = [
    '"Aaja Sanam Madhur Chandni Mein Hum" from Chori Chori (1956)',
    '"Chhod Do Aanchal Zamana Kya Kahega" from Paying Guest (1957)',
    '"Chhodo Kal Ki Baatein" from Hum Hindustani (1960)',
    '"Ae Meri Zohra Jabeen" from Waqt (1965)',
    '"Jahan Mein Jati Hoon" from Chori Chori (1956)',
    '"Ajeeb Dastan Hai Yeh" from Dil Apna Aur Preet Parai (1960)',
    '"Chaudhvin Ka Chand Ho" from Chaudhvin Ka Chand (1960)',
    '"Pyar Hua Ikrar Hua" from Shree 420 (1955)'
]

C_1970_1999 = [
    '"Mere Sapno Ki Rani" from Aradhana (1969)',
    '"Chala Jata Hoon Kisi Ki Dhun Mein" from Mere Jeevan Saathi (1972)',
    '"Yeh Dosti" from Sholay (1975)',
    '"Yeh Shaam Mastani" from Kati Patang (1971)',
    '"Dilbar Mere" from Satte Pe Satta (1982)',
    '"Mehbooba Mehbooba" from Sholay (1975)',
    '"Ek Ladki Ko Dekha" from 1942: A Love Story (1994)',
    '"Rimjhim Gire Saawan" from Manzil (1979)',
    '"Hum Tum Ek Kamre Mein" from Bobby (1973)',
    '"Pehla Nasha" from Jo Jeeta Wohi Sikandar (1992)'
]

C_2000_2013 = [
    '"Tera Hone Laga Hoon" from Ajab Prem Ki Ghazab Kahani (2009)',
    '"All Is Well" from 3 Idiots (2009)',
    '"Tumhi Ho Bandhu" from Cocktail (2012)',
    '"Jab Koi Baat Bigad Jaye" from Jurm (2005)',
    '"Pee Loon" from Once Upon a Time in Mumbaai (2010)',
    '"Agar Tum Mil Jao" from Zeher (2005)',
    '"Tum Mile" from Tum Mile (2009)'
]

C_2014_2024 = [
    '"Sau Aasmaan" from Baar Baar Dekho (2016)',
    '"Tera Ban Jaunga" from Kabir Singh (2019)',
    '"Sun Saathiya" from ABCD 2 (2015)',
    '"Samjhawan" from Humpty Sharma Ki Dulhania (2014)',
    '"Hasi Ban Gaye" from Hamari Adhuri Kahani (2015)',
    '"Raabta" from Raabta (2017)',
    '"Kaun Tujhe" from M.S. Dhoni: The Untold Story (2016)',
    '"Dil Diyan Gallan" from Tiger Zinda Hai (2017)',
    '"Ve Maahi" from Kesari (2019)',
    '"Pal" from Jalebi (2018)'
]

Happy = {
    "Black & White Era(1955-1970)": H_1955_1970,
    "90s Era(1970-1999)": H_1970_1999,
    "Era of 2000s(2000-2013)": H_2000_2013,
    "Golden Era(2014-2024)": H_2014_2024
}

Sad = {
    "Black & White Era(1955-1970)": S_1955_1970,
    "90s Era(1970-1999)": S_1970_1999,
    "Era of 2000s(2000-2013)": S_2000_2013,
    "Golden Era(2014-2024)": S_2014_2024
}

Calming = {
    "Black & White Era(1955-1970)": C_1955_1970,
    "90s Era(1970-1999)": C_1970_1999,
    "Era of 2000s(2000-2013)": C_2000_2013,
    "Golden Era(2014-2024)": C_2014_2024
}

MOOD_CATALOG = {
    "Happy": Happy,
    "Sad": Sad,
    "Calming": Calming
}

ERA_KEYS = [
    "Black & White Era(1955-1970)",
    "90s Era(1970-1999)",
    "Era of 2000s(2000-2013)",
    "Golden Era(2014-2024)"
]


def userChoice(user_name):
    """Ask user's current mood and the era of songs with input validation."""
    valid_moods = ["Happy", "Sad", "Calming"]
    while True:
        mood = input(f"\nWelcome {user_name}! What's your mood today?\n- Happy\n- Sad\n- Calming\nEnter your mood: ").strip().capitalize()
        if mood in valid_moods:
            break
        print("Invalid choice! Please choose from Happy, Sad, or Calming.")

    print("\nWe have classified songs according to era as:")
    for idx, era_name in enumerate(ERA_KEYS, start=1):
        print(f"  {idx}. {era_name}")

    while True:
        era_input = input("\nWhich one do you want to choose (1, 2, 3, or 4): ").strip()
        if era_input in ["1", "2", "3", "4"]:
            era = int(era_input)
            break
        print("Invalid era selection! Please enter a number between 1 and 4.")

    return mood, era


def generateRandomPlaylist(user_name, mood, era, count=5):
    """Generate a playlist with randomly selected unique songs."""
    era_name = ERA_KEYS[era - 1]
    song_pool = MOOD_CATALOG[mood][era_name]
    num_to_pick = min(count, len(song_pool))
    playlist = random.sample(song_pool, num_to_pick)

    print(f"\nHey {user_name}! Here is your personalized {mood} playlist ({era_name}):")
    for i, song in enumerate(playlist, start=1):
        print(f"  {i}. {song}")

    return playlist


def addMusic(playlist):
    """Add N custom songs to the playlist."""
    while True:
        try:
            num = int(input("\nEnter number of songs you want to add: ").strip())
            if num >= 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    for i in range(num):
        song = input(f"Enter song #{i + 1}: ").strip()
        if song:
            playlist.append(f'"{song}" (User Added)')
    return playlist


def editPlaylist(playlist):
    """Allow user to shuffle or reverse their playlist."""
    print("\nPlaylist customization options:")
    print("  1. Shuffle playlist")
    print("  2. Reverse playlist")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        random.shuffle(playlist)
        print("Playlist shuffled successfully!")
    elif choice == "2":
        playlist.reverse()
        print("Playlist reversed successfully!")
    else:
        print("Invalid choice. Playlist kept as is.")
    return playlist


def exportPlaylist(user_name, playlist, filename="playlist.txt"):
    """Export the playlist to a text file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"=== {user_name}'s Music Playlist ===\n\n")
            for idx, song in enumerate(playlist, start=1):
                f.write(f"{idx}. {song}\n")
        print(f"\nPlaylist successfully saved to '{filename}'!")
    except IOError as e:
        print(f"Failed to save playlist: {e}")


def displayPlaylist(playlist):
    """Display the current playlist in a neat numbered format."""
    print("\nCurrent Playlist:")
    for idx, song in enumerate(playlist, start=1):
        print(f"  {idx}. {song}")


def main():
    print("=" * 45)
    print("🎵 Welcome to Music Playlist Generator 🎵")
    print("=" * 45)

    name = input("Enter your name: ").strip().capitalize()
    if not name:
        name = "Friend"

    while True:
        mood, era = userChoice(name)
        playlist = generateRandomPlaylist(name, mood, era)

        # Add custom songs
        choice1 = input("\nDo you want to add custom music to your playlist? (Yes/No): ").strip().capitalize()
        if choice1 == "Yes":
            playlist = addMusic(playlist)
            displayPlaylist(playlist)

        # Shuffle or reverse
        choice2 = input("\nDo you want to shuffle or reverse your playlist? (Yes/No): ").strip().capitalize()
        if choice2 == "Yes":
            playlist = editPlaylist(playlist)
            displayPlaylist(playlist)

        # Export playlist
        choice3 = input("\nDo you want to save this playlist to a text file? (Yes/No): ").strip().capitalize()
        if choice3 == "Yes":
            exportPlaylist(name, playlist)

        # Generate another
        repeat = input("\nDo you want to generate another playlist? (Yes/No): ").strip().capitalize()
        if repeat != "Yes":
            print(f"\nThank you for using Music Playlist Generator, {name}! Enjoy your tunes! 🎧")
            break


if __name__ == "__main__":
    main()