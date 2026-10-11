# 🎵 Music Playlist Generator

A console-based Python application that generates personalized song playlists based on your mood and preferred music era, with an optional shuffle to keep every listening session fresh.

## Overview

Choosing what to listen to can be harder than it sounds. This project takes a simple approach: tell the program how you're feeling, pick the era of music you enjoy, and it builds a playlist for you. It's a beginner-friendly project that demonstrates core Python concepts such as user input handling, data structures, functions, and randomization.

## Features

- **Mood-based playlists:** Get songs that match your current mood (Happy, Sad, Calming).
- **Era selection:** Choose your preferred music period across 4 distinct eras (1955 to 2024).
- **Add custom songs:** Expand your playlist with your own favorite tracks.
- **Shuffle & Reverse options:** Reorder or randomize your playlist on the fly.
- **File Export:** Save your customized playlist to `playlist.txt`.
- **Menu-driven interface:** Simple, interactive prompts in the console.
- **Input validation:** Handles invalid choices gracefully and prompts you to try again.

## Tech Stack

- **Language:** Python 3
- **Modules:** `random`

## Getting Started

### Prerequisites

- Python 3.x installed on your system ([download here](https://www.python.org/downloads/))

### Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Zaara-Abrar/Music-Playlist-Generator.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Music-Playlist-Generator
   ```
3. Run the program:
   ```bash
   python MusicPlaylistGenerator.py
   ```

## How It Works

1. Enter your name.
2. Select your current **mood** (`Happy`, `Sad`, or `Calming`).
3. Pick your preferred **era** (1 to 4):
   - 1. Black & White Era (1955-1970)
   - 2. 90s Era (1970-1999)
   - 3. Era of 2000s (2000-2013)
   - 4. Golden Era (2014-2024)
4. A personalized 5-song playlist is generated.
5. Optionally add custom songs, shuffle, reverse, or export the playlist to a file!

## Example Walkthrough

```text
=============================================
🎵 Welcome to Music Playlist Generator 🎵
=============================================
Enter your name: Alex

Welcome Alex! What's your mood today?
- Happy
- Sad
- Calming
Enter your mood: Happy

We have classified songs according to era as:
  1. Black & White Era(1955-1970)
  2. 90s Era(1970-1999)
  3. Era of 2000s(2000-2013)
  4. Golden Era(2014-2024)

Which one do you want to choose (1, 2, 3, or 4): 2

Hey Alex! Here is your personalized Happy playlist (90s Era(1970-1999)):
  1. "Chaiyya Chaiyya" from Dil Se (1998)
  2. "Aap Jaisa Koi" from Qurbani (1980)
  3. "Humko Tumse Ho Gaya Hai Pyar" from Amar Akbar Anthony (1977)
  4. "Ina Mina Dika" from Amar Akbar Anthony (1977)
  5. "Jai Jai Shiv Shankar" from Aap Ki Kasam (1974)

Do you want to add custom music to your playlist? (Yes/No): No

Do you want to shuffle or reverse your playlist? (Yes/No): Yes

Playlist customization options:
  1. Shuffle playlist
  2. Reverse playlist
Enter your choice (1 or 2): 1
Playlist shuffled successfully!

Current Playlist:
  1. "Jai Jai Shiv Shankar" from Aap Ki Kasam (1974)
  2. "Aap Jaisa Koi" from Qurbani (1980)
  3. "Chaiyya Chaiyya" from Dil Se (1998)
  4. "Ina Mina Dika" from Amar Akbar Anthony (1977)
  5. "Humko Tumse Ho Gaya Hai Pyar" from Amar Akbar Anthony (1977)

Do you want to save this playlist to a text file? (Yes/No): Yes
Playlist successfully saved to 'playlist.txt'!

Do you want to generate another playlist? (Yes/No): No
Thank you for using Music Playlist Generator, Alex! Enjoy your tunes! 🎧
```

## Future Improvements

- Add genre and artist filters
- Integrate with Spotify / YouTube API for instant streaming links
- Build a graphical interface (GUI) or web version

## Author

**Zaara Abrar**
- GitHub: [Zaara-Abrar](https://github.com/Zaara-Abrar)
- LinkedIn: [zaara-abrar](https://linkedin.com/in/zaara-abrar-091186259)
