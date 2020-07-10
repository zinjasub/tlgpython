#!/usr/bin/python3

def main():
    movies = [] # one way to create a list
    movies.append("Avatar")  #.append is a list method that applies the value passed to it at the END of the list

    movies.append("Back to the Future")

    print(movies)
    
    print(movies[0])

    movies.append("Ghostbusters")

    print(movies[2])

    print(movies[-1])

    print(movies.index("Ghostbusters"))



if __name__ == "__main__":
    main()


