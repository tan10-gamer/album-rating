# get_valid_rating function to ensure the user inputs a valid rating between 1 and 10
def get_valid_rating():
    while True:
        try:
            rating = int(input("Enter your rating for the album (1-10):"))
            if 1 <= rating <=10:
                return rating
            else:
                print("Invalid rating. Please enter a rating between 1 and 10.")
        except ValueError:
            print("Please enter a number.")          # handles user's input


# recommend_album function to provide a recommendation based on the rating
def recommend_album(rating):
    if rating >= 8:
        print("Good! Would recommend this album.")
        return True
    elif rating >= 5:
        print("Fair. Might recommend this album.")
        return False
    else:
        print("Bad. Would not recommend this album.")
        return False

# album_rating function to get album title, artist name, and rating from the user and provide a summary and recommendation summary    
def album_rating():
    album_title = input("Enter the album title: ")
    artist_name = input("Enter the artist name: ")

    # condition to check that rating stays between 1 and 10
    rating = get_valid_rating()

    print("\n----Album Summary----")
    print("Album Title: ", album_title)
    print("Artist Name: ", artist_name)
    print("Rating: ", rating)

    print("\n----Recommendation----")
    recommend = recommend_album(rating)         # recommendation returns True or False based on the rating

    # decision statement to recommend more albums by the artist based on user input
    if recommend:
        print("You might also like other albums by this artist.")
    else:
        print("You might not like other albums by this artist.")


album_rating()   # calls the album_rating function to start the program


# main program. Loop to ask the user if they want to rate another album or exit the program
while True:
    next_album = input("\nWould you like to rate another album? (yes/no): ")
    if next_album == "yes":
            album_rating()
    elif next_album == "no":
        print("Thank you for using the album rating program!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
