# Hangmanenator 2000
A simple Python script made for making Hangamanen easier for Roulette hosts. 

A Roulette a game in Dream Theater Forums' General Music Discussion section, in which a host gathers several players, and per round, the host receives a song from each player. He gives them several listens, then scores them according to personal preference. The goal of Roulettes is to discover new music, and as scores are accumulative, the player who sends the best songs wins.

Part of the fun in recent years is playing a variant of the classic Hangman, in which the players have to guess what songs were sent to the guest, and by who, before he posts results. Because this was a tedious, error-prone process by hand, this little script was born to help that. 

To use it, place a text file in the same folder as script, and put the entries for the round using the following format, one per line:
```
Player: Artist - Song
```
First, clone it into a folder you like
```
git clone https://github.com/Sacules/hangmanen.git
```
or download it as a ZIP file. Afterwards, open a terminal in the folder that was created and run the script with
```
python3 hangmanen.py
```
If you're using Linux, it's likely your distro already comes with Python 3.x and git installed. On Windows and OSX, you can download Python from [here](https://www.python.org/downloads/) (make sure you choose the option "Add to PATH" when installing!) and git from [here](https://git-scm.com/downloads).

## Example
Let's look at one of the rounds I hosted - I made a file called _round 4.txt_, opened it, and saved the following:

```
Parama: The Hirsch Effekt - Irrath
Bolsters, the Traitor: Amy Shark - Deleted
Nekov: Angra - Wishing Well
Train of Naught: Trivium - The Sin and the Sentence
Evermind: Seventh Wonder - Alley Cat
Tomislav95: Iced Earth - A Question of Heaven
Luoto: Insomnium - Revelation
ariich: Amorphis - Dark Path
home: Blind Guardian -  The Bard's Song - In the Forest
kingshmegland: Pagan's Mind - Through Osiris' Eyes
Kattoelox: Aquaria - Expedition
Elite: Caligula's Horse - A Gift to Afterthought
```

Using the script, it generates this:

```
?: ___ ______ ______ - ______
?: ___ _____ - _______
?: _____ - _______ ____
?: _______ - ___ ___ ___ ___ ________
?: _______ ______ - _____ ___
?: ____ _____ - _ ________ __ ______
?: _________ - __________
?: ________ - ____ ____
?: _____ ________ -  ___ ____'_ ____ - __ ___ ______
?: _____'_ ____ - _______ ______' ____
?: _______ - __________
?: ________'_ _____ - _ ____ __ ____________
```

After guessing some letters, artists, songs, and players:

```
Parama: The Hirsch Effekt - Irrath
Bolsters, Traitor: Amy Shark - ____t__
?: Angra - __s__n_ ____
?: Trivium - The Sin and the Sentence
?: S___nt_ __n___ - A____ _at
?: ____ _a_t_ - A ___st__n __ __a__n
?: Insomnium - Revelation
?: Amorphis - Dark Path
?: Blind Guardian -  The Bard's Song - In the Forest
?: Pagan's Mind - Through Osiris' Eyes
?: A__a__a - ______t__n
?: Caligula's Horse - A Gift to Afterthought

Guessed letters: M B A S N T
```

The script saves the guessed letters and words in a separate file from the guessed players.
