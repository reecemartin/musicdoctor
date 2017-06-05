import ast


def get_catalogue():
    """
    Returns the artist catalogue

    :return: dict
    """

    return ast.literal_eval(open('data.dat').readline())


def get_points(database, source):
    """
    Compares the scores for the user entered artist and all other artists in the database in order to
    find the most closely related artists.

    :param dict database: Database of all artist's stats
    :param list of str source: Name of artist
    :return: dict of int: list of str
    """
    point_distri = {}
    for artist in database:
        if artist not in source:
            artist_dat = database[artist]  # Shortcut for current artist
            points = 0  # Start at 0 points different
            if source[0] != "":
                for guy in source:
                    source_dat = database[guy]  # Shortcut for source

                for modifier in artist_dat:
                    # For each stat
                    if modifier != 'NAME':  # As long as it's not the artist name
                        points += abs(artist_dat[modifier] - source_dat[modifier])  # Add difference in stats to points

            # Assign the artist to their respective points
            if len(source) != 0:
                try:
                    point_distri[points / len(source)].append(artist)
                except KeyError:
                    point_distri[points / len(source)] = [artist]

    return point_distri


if __name__ == "__main__":

    database = get_catalogue()
    favoured_artists = []

    # First prompt the user for a source artist
    print('Welcome to Music Doctor, enter "Exit" to exit. Enter "Suggest [Number of Suggestions]" to get '\
           'suggestions. Enter Catalogue to see all artists. Enter "Random" for a random artist.')

    while True:

        # Input is cleaned by converting to lowercase and removing whitespace
        source = input("I want artists like:\n").upper().strip()


        # Splits Suggest and the number of suggestions requested
        if "SUGGEST" in source:
            num_suggestions = source.split(" ")[1]
            source = source.split(" ")[0]

        # Breaks loop if user enters -1
        if source == "EXIT":
            break
            

        # Prints the current Catalogue
        elif source == "CATALOGUE":
            point_distri = get_points(database, [""])
            points = sorted(list(point_distri.keys()))
            print("Catalogue:\n")

            for artist in point_distri[0.0]:
                print(artist)

            print("\n\n")
            
        elif source == "Random":
            point_distri = get_points(database, [""])
            points = sorted(list(point_distri.keys()))
            print("Catalogue:\n")

            random_artist = random.randrange(start, len(point_distri[0.0]))
            print(point_distri[0.0][random_artist])

            print("\n\n")

        elif source == 'SUGGEST' and len(favoured_artists) > 0:
            point_distri = get_points(database,
                                      favoured_artists)  # Get difference of points between chosen artist and the rest
            points = sorted(list(point_distri.keys()))  # Sort the difference by lowest->highest difference

            print("Here are some suggestions:")

            # Show each artist from least difference in points to most and the percentage they matched the chosen artist
            count = 1
            for point in points:
                percent = ((9 * (len(database[favoured_artists[0]]) - 1) - point) / (
                9 * (len(database[favoured_artists[0]]) - 1))) * 100
                for artist in point_distri[point]:
                    print(str(count) + '. ' + artist + ' - Percentage matched: ' + str("%.2f" % percent + '%'))
                    count += 1

                # Allows user to choose number of artists returned
                if count >= int(num_suggestions) + 1:
                    break

            print()

        elif source == 'SUGGEST':
            print('Add an artist first!')

        elif source not in database:
            print('Invalid artist!')

        elif source in database:
            favoured_artists.append(source)
            print('Artist added!')

        else:
            raise Exception('Ding Dong! The errors are ringing')
