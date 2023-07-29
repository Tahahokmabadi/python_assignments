import operator

def add_movie():
    movie = input("Enter the movie name: ")
    score = float(input("Enter the IMDB score: "))
    with open("movie.txt", "a") as file:
        file.write("\n")
        file.write(f"{movie} : {score}\n")
    print("Movie added successfully!")

def show_information():
    with open("movie.txt", "r") as file:
         print(file.read())

def show_highest_scores():
    scores = {}
    with open("movie.txt", "r") as file:
        for line in file:
             movie, score = line.strip().split(" : ")
             scores[movie] = float(score)
    
    sorted_scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
    print("Top 5 movies with highest scores:")
    for i, (movie, score) in enumerate(sorted_scores[:5]):
        print(f"{i+1}. {movie} - {score}")

def show_alphabetical_order():
    movies = []
    with open("movie.txt", "r") as file:
        for line in file:
            movie, _ = line.strip().split(" : ")
            movies.append(movie)
    sorted_movies = sorted(movies)
    
    print("Movies in alphabetical order:")
    for i, movie in enumerate(sorted_movies):
        print(f"{i+1}. {movie}")

while True:
    print("\nOptions:")
    print("1. Add the movie and IMDB score to file")
    print("2. Show the information stored in the file")
    print("3. Show the 5 movies with the highest scores")
    print("4. Show the names of the movies in alphabetical order")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        add_movie()
    elif choice == "2":
        show_information()
    elif choice == "3":
        show_highest_scores()
    elif choice == "4":
        show_alphabetical_order()
    elif choice == "5":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice! Please try again.")
        movie.txt