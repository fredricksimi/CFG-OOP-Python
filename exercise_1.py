

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name is {self.name} and they server {self.cuisine}")


    def open_restaurant(self):
        print("This restaurant is open, yaaaaaaay")

restaurant = Restaurant('Usta', 'Turkish')
print(f"The name of the restaurant is {restaurant.name}")
print(f"The type of cuisine is {restaurant.cuisine}")

restaurant.describe_restaurant()
restaurant.open_restaurant()