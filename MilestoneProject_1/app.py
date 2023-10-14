# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code


def add_movies():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


# Create other functions for:

#   - listing movies
def list_movies():
    for movie in movies:
        print_movie(movie)

#   - finding movies
def find_movie():
    user_input = input("Please Enter your movie name: ")
    for movie in movies:
        if user_input == movie["title"]:
            print_movie(movie)

def print_movie(movie):
    print(f"title : {movie['title']}")
    print(f"director : {movie['director']}")
    print(f"year : {movie['year']}")


# And another function here for the user menu
user_options = {
    "a" : add_movies,
    "l" : list_movies,
    "f" : find_movie
}
def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selection_operation = user_options[selection]
            selection_operation()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu()