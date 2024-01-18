def make_album(artist_name, album_title, number_songs=None):
    """Builds a describing a music album."""
    item = {
        "Artist name": artist_name.title(),
        "Album title": album_title.title()
    }
    if number_songs:
        item["Number of songs"] = number_songs

    return item

while True:
    print("\nPlease enter the follow information:")
    print("((Enter 'q' to quit))")
    a_name = input("Enter Artist's name: ")
    if a_name == 'q':
        break
    album_name = input("Enter album's title: ")
    if album_name == 'q':
        break
    number_songs = input("Enter number of songs: ")
    if number_songs == 'q':
        break

    new_album = make_album(a_name, album_name, number_songs)
    print(new_album)
    print("\nThank you")
