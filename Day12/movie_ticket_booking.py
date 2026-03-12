'''Design a Movie Ticket Booking System.
The system should:
1. Store multiple movies.
2. For each movie store:
   Ticket price
   Total seats available
3. Allow customers to:
   Select a movie
   Enter number of tickets
4. Calculate:
   Total bill
   Remaining seats
5. Prevent overbooking.
6. At the end, display:
   Total revenue generated
   Movie with highest bookings'''

print("Movie Ticket Booking System")

movies = {
    "Leo": {"price": 200, "seats": 50, "booked": 0},
    "Jailer": {"price": 150, "seats": 40, "booked": 0},
    "Vikram": {"price": 180, "seats": 30, "booked": 0}
}

total_revenue = 0

def show():
    print("\nAvailable Movies:")
    for name, details in movies.items():
        print(name,
              "- Price:", details["price"],
              "- Seats:", details["seats"])


def book():
    global total_revenue #modifying a variable that was defined outside the function
    
    movie_name = input("Enter movie name: ")
    
    if movie_name not in movies:
        print("Movie not found.")
        return
    
    tickets = int(input("Enter number of tickets: "))
    
    available = movies[movie_name]["seats"]
    
    if tickets > available:
        print("Not enough seats available.")
        return
    
    cost = tickets*movies[movie_name]["price"]
    
    movies[movie_name]["seats"] -= tickets
    movies[movie_name]["booked"] += tickets
    total_revenue += cost
    
    print("Booking Successful")
    print("Total Cost:", cost)


def summary():
    print("\nFinal Summary")
    print("Total Revenue:", total_revenue)
    
    most = ""
    max_tickets = 0
    
    for name, details in movies.items():
        if details["booked"] > max_tickets:
            max_tickets = details["booked"]
            most = name
    
    print("Most Popular Movie:", most)
    
    print("\nRemaining Seats:")
    for name, details in movies.items():
        print(name, ":", details["seats"])


while True:
    print("\n1. Show Movies")
    print("2. Book Ticket")
    print("3. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        show()
    elif choice == "2":
        book()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")

summary()
