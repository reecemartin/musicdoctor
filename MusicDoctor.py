def get_catalogue():
    """
    Returns the artist catalogue

    :return: List of Tuple
    :rtype: List of Tuple
    """
    # Artist Attributes in Catalogue:
    # ===============================

    # Artist Name / How sad / How heavy (i.e. pop would be light) / How much artistic license
    # / How popular / How much electronic influence

    # Each of the prior scores is on a float scale from 1 - 10

    catalogue = [("alt-J", 5.6, 3.0, 6.0, 5.0, 6.0),\
                 ("Arcade Fire", 6.5, 4.0, 6.5, 5.0, 6.0),\
                 ("Arctic Monkeys", 4.0, 7.0, 4.0, 6.5, 3.0),\
                 ("Blur", 3.0, 6.5, 4.5, 7.0, 2.0),\
                 ("Bon Iver", 7.5, 3.0, 7.0, 5.0, 5.0),\
                 ("Childish Gambino", 2.0, 6.0, 3.0, 6.5, 5.0),\
                 ("Death Cab for Cutie", 8.0, 5.0, 5.0, 4.0, 6.0),\
                 ("Foster The People", 2.0, 2.0, 7.5, 6.5, 8.0),\
                 ("Glass Animals", 1.8, 2.4, 7.2, 5.0, 6.0),\
                 ("Gorillaz", 6.0, 5.0, 8.2, 6.8, 7.6),\
                 ("Interpol", 6.0, 5.7, 5.3, 4.3, 3.3),\
                 ("Jack White", 4.5, 7.6, 6.5, 6.6, 3.2),\
                 ("Kendrick Lamar", 1.3, 7.3, 4.5, 8.0, 5.0),\
                 ("LCD Soundsystem", 5.6, 4.7, 5.8, 5.2, 8.2),\
                 ("Logic", 1.0, 2.5, 6.2, 5.8, 6.8),\
                 ("M83", 5.6, 5.0, 7.8, 3.4, 9.2),\
                 ("Modest Mouse", 7.2, 6.2, 6.4, 3.2, 2.2),\
                 ("Nirvana", 6.0, 7.2, 6.3, 7.5, 1.1),\
                 ("Oasis", 3.5, 5.4, 3.2, 7.2, 2.0),\
                 ("Passion Pit", 7.3, 1.4, 6.5, 2.3, 8.2),\
                 ("Queens of the Stone Age", 3.5, 5.6, 5.7, 5.4, 2.1),\
                 ("Radiohead", 9.5, 7.8, 8.2, 7.0, 7.2),\
                 ("The Smashing Pumpkins", 5.4, 6.2, 4.3, 5.2, 3.4),\
                 ("Vampire Weekend", 2.2, 2.0, 6.8, 5.5, 3.2),\
                 ("Weezer", 7.0, 6.5, 2.2, 4.2, 2.1),\
                 ("The White Stripes", 1.2, 7.8, 5.8, 6.0, 2.3)]

    return catalogue

if __name__ == "__main__":

    # Loop allows for repeated suggestions
    active = True
    while active is True:

        # First prompt the user for a source artist
        print("Welcome to Music Doctor, enter -1 to exit.")

        # Input is cleaned by converting to lowercase and removing whitespace
        source = input("I want artists like:").lower().strip().replace(" ", "")
        print("Here are some suggestions:")

        # Breaks loop if user enters -1
        if source == "-1":
            active = False
            break

        else:

            database = get_catalogue()

            # Get the attributes for that artist
            artist_store = [0, 0, 0, 0, 0]
            for a in database:
                if a[0].lower().strip().replace(" ", "") == source:
                    artist_store[0], artist_store[1], artist_store[2], artist_store[3], artist_store[4] = \
                        a[1], a[2], a[3], a[4], a[5]
                    break

            queue = []
            for a in database:
                if len(queue) == 0:
                    queue.append((a[0], abs(artist_store[0] - a[1]) +
                                  abs(artist_store[1] - a[2]) + abs(artist_store[2] - a[3]) +
                                  abs(artist_store[3] - a[4]) + abs(artist_store[4] - a[5])))
                else:
                    current_artist = (a[0], abs(artist_store[0] - a[1]) +
                                      abs(artist_store[1] - a[2]) + abs(artist_store[2] - a[3]) +
                                      abs(artist_store[3] - a[4]) + abs(artist_store[4] - a[5]))
                    i = 0
                    while i < len(queue):
                        if current_artist[1] < queue[i][1]:
                            queue.insert(i, current_artist)
                            break
                        i += 1

            queue.pop(0)
            for x in range(5):
                print(queue[x][0])
            print("\n \n")
