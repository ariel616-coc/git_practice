liked_songs = {
    "Shake It Off": {
        "artist": "Taylor Swift",
        "duration": (3, 23),
        "genre": "Pop"
    },
    "Shemesh": {
        "artist": "Mergi",
        "duration": (2, 33),
        "genre": "Israeli"
    },
    "Chop Suey!": {
        "artist": "System of a Down",
        "duration": (3, 30),
        "genre": "Metal"
    },
    "Mimaamakim": {
        "artist": "Idan Raichel",
        "duration": (4, 33),
        "genre": "Israeli"
    },
    "Do I Wanna Know?": {
        "artist": "Arctic Monkeys",
        "duration": (4, 26),
        "genre": "Rock"
    },
    "Love Story": {
        "artist": "Taylor Swift",
        "duration": (3, 55),
        "genre": "Pop"
    },
    "Bo’ee": {
        "artist": "Idan Raichel",
        "duration": (4, 45),
        "genre": "Israeli"
    }
}

def create_songs_dictionary():
    song_dictionary = {}

    while True:
        name = input("enter the name of the song: ")
        if name in liked_songs:
            print("the song is already im the playlist")
        else:
            break

    artist = input("enter the name of the artist: ")
    while True:
        minutes = input("enter how much full minutes the song take long? ")
        if minutes.isdigit():
            minutes = int(minutes)
            break
        else:
            print("enter number.")

    while True:
        seconds = input("enter how much seconds (not full minute) the song take long? ")
        if seconds.isdigit() and int(seconds) < 60:
            seconds = int(seconds)
            break
        else:
            print("enter number between 0 to 59.")

    duration = (minutes, seconds)
    genre = input("enter the genre of the song: ")


    song_dictionary[name] = {"artist":artist,"duration":duration,"genre":genre}

    print(song_dictionary)
    return song_dictionary


def print_playlist():
    for song in liked_songs:
        print(f"{song}:\n   artist = {liked_songs[song]["artist"]}\n   duration = {liked_songs[song]["duration"]}\n   genre = {liked_songs[song]["genre"]}\n")


def check_if_song_in_playlist_by_name_and_remove():
    name = input("enter the name of the song: ")
    if name in liked_songs:
        print("the song in the playlist.")
        liked_songs.pop(name)
        return
    else:
        print("the song is not in the playlist.")
        return


def remove_the_artists_songs():
    artist_to_remove = input("enter the name of the artist: ")
    for song in liked_songs:
        if liked_songs[song]["artist"] == artist_to_remove:
            liked_songs.pop(song)
            return

    print("you dont have the artist's songs in your playlist.")
    return


def main():
    while True:
        time = input("how much songs do you want to add? ")
        if time.isdigit():
            time = int(time)
            break
        else:
            print("enter number.")

    for songs_add in range(time):
        song_dictionary = create_songs_dictionary()
        for i in song_dictionary:
            name = i

        liked_songs[name] = song_dictionary[name]

    print_playlist()

    check_if_song_in_playlist_by_name_and_remove()

    remove_the_artists_songs()





main()