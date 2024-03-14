print("Welcome to the Holiday Cost Calculator!"
"Planning your dream vacation? Let us help you estimate the total cost of your holiday adventure." 
"Simply answer a few quick questions below, and we'll provide you with an estimate tailored to your preferences and budget.")
city_flight = input("Choose a destination from the list: Paris, Lisbon, Milan, Oslo ")
num_nights = int(input("Enter the number of nights for your stay "))
rental_days = int(input("Enter the number of days for your car rental "))
def hotel_cost(num_nights, hotel_rate = 128):
    hotel = num_nights * hotel_rate
    return(hotel)
def plane_cost(city_flight):
    if city_flight == "Paris":
        return 120  # Example cost for a flight to Paris
    elif city_flight == "Lisbon":
        return 110  # Example cost for a flight to Lisbon
    elif city_flight == "Milan":
        return 180  # Example cost for a flight to Milan
    elif city_flight == "Oslo":
        return 210  # Example cost for a flight to Oslo
    else:
        return "City not supported"  # Return this if the chosen city is not in the list
def car_rental(rental_days, rental_rate = 88):
    car = rental_days * rental_rate
    return car
def total_holiday_cost(hotel_cost, plane_cost, car_rental):
    total = hotel_cost + plane_cost + car_rental
    return total
total_cost = total_holiday_cost(hotel_cost(num_nights), plane_cost(city_flight), car_rental(rental_days))
print (f"The total cost of your trip to {city_flight} for {num_nights} nights with a {rental_days}-day car rental is £{total_cost}")

