
class Movie:
    def __init__(self, title, director, release_year, budget, box_office_earnings):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.budget = budget
        self.box_office_earnings = box_office_earnings
        # self.movie_enjoyed = True


    def get_movie_details(self):
        print(f"{self.title} was released in {self.release_year} and was directed by {self.director}")

    def calculate_profit(self):
        if self.box_office_earnings > self.budget:
            profit = self.box_office_earnings - self.budget
            print(f"{self.title} made a profit of ${profit} in the box office 😎")
        else:
            print(f"{self.title} made a loss in the box office 😭")

    # def movie_opinion(self):
    #     if self.movie_enjoyed == True:
    #         print("I enjoyed the movie")
    #     else:
    #         print("I didn't enjoy the movie")

my_movie = Movie('Avengers:Endgame', 'The Russo Brothers', 2019, 356000000, 2800000000)
my_movie.get_movie_details()
my_movie.calculate_profit()
#my_movie.movie_opinion()
