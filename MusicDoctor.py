import ast


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

    return ast.literal_eval(open('data.dat').readline())


def get_points(database, source):
    """
    Get the difference between each artist in database and source
    
    :param dict database: Database of all artist's stats
    :param str source: Name of artist
    :return: dict of int: list of str
    """

    point_distri = {}
    source_dat = database[source]  # Shortcut for source

    for artist in database:
        if artist != source:
            points = 0  # Start at 0 points different
            artist_dat = database[artist]  # Shortcut for current artist

            for modifier in artist_dat:
                # For each stat
                if modifier != 'NAME':  # As long as it's not the artist name
                    points += abs(artist_dat[modifier] - source_dat[modifier])  # Add difference in stats to points

            # Assign the artist to their respective points
            try:
                point_distri[points].append(artist)
            except KeyError:
                point_distri[points] = [artist]

    return point_distri

if __name__ == "__main__":

    # Loop allows for repeated suggestions
    active = True
    database = get_catalogue()

    # First prompt the user for a source artist
    print("Welcome to Music Doctor, enter \"kys\" to exit.")

    while True:

        # Input is cleaned by converting to lowercase and removing whitespace
        source = input("I want artists like:\n").upper().strip().replace(" ", "").split()[0]

        # Breaks loop if user enters -1
        if source == "KYS":
            break

        elif source not in database:
            print('Invalid artist!')

        else:
            point_distri = get_points(database, source)  # Get difference of points between chosen artist and the rest
            points = sorted(list(point_distri.keys()))  # Sort the difference by lowest->highest difference

            print("Here are some suggestions:")

            # Show each artist from least difference in points to most and the percentage they matched the chosen artist
            count = 1
            for point in points:
                percent = ((9 * (len(database[source]) - 1) - point) / (9 * (len(database[source]) - 1))) * 100
                for artist in point_distri[point]:
                    print(str(count) + '. ' + artist + ' - Percentage matched: ' + str("%.2f" % percent))
                    count += 1

            print()
