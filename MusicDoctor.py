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


if __name__ == "__main__":

    # Loop allows for repeated suggestions
    active = True
    database = get_catalogue()

    # First prompt the user for a source artist
    print("Welcome to Music Doctor, enter \"kys\" to exit.")

    while active is True:

        # Input is cleaned by converting to lowercase and removing whitespace
        source = input("I want artists like:\n").upper().strip().replace(" ", "").split()[0]

        # Breaks loop if user enters -1
        if source == "KYS":
            active = False
            break

        elif source not in database:
            print('Invalid artist!')

        else:
            point_distri = {}
            source_dat = database[source]

            for artist in database:
                if artist != source:
                    points = 0
                    artist_dat = database[artist]

                    for modifer in artist_dat:
                        if modifer != 'NAME':
                            points += abs(artist_dat[modifer] - source_dat[modifer])\

                    try:
                        point_distri[points].append(artist)
                    except KeyError:
                        point_distri[points] = [artist]

            points = sorted(list(point_distri.keys()))

            print("Here are some suggestions:")

            count = 1
            for point in points:
                percent = ((50 - point) / 50) * 100
                for artist in point_distri[point]:
                    print(str(count) + '. ' + artist + ' - Percentage matched: ' + str("%.2f" % percent))
                    count += 1

            print()
