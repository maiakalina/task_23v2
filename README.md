# Holiday Cost Calculator

This Python application helps you estimate the total cost of your holiday. It prompts users to answer a few questions about their travel preferences and calculates the total cost based on the provided inputs.

## Usage

1. Run the program in your Python environment.
2. Follow the prompts to provide the necessary information:
   - Choose a destination city from the provided list (Paris, Lisbon, Milan, Oslo).
   - Enter the number of nights for your stay.
   - Enter the number of days for your car rental.
3. The program will calculate and display the total cost of your trip.

## Program Logic

The program consists of the following functions:

- `hotel_cost(num_nights, hotel_rate)`: Calculates the cost of the hotel stay based on the number of nights.
- `plane_cost(city_flight)`: Determines the cost of the flight based on the chosen destination city.
- `car_rental(rental_days, rental_rate)`: Calculates the cost of the car rental based on the number of days.
- `total_holiday_cost(hotel_cost, plane_cost, car_rental)`: Calculates the total cost of the holiday based on the individual costs.

## Example

```python
print("This application will help you calculate the cost of your holiday. Please answer the questions below.")
city_flight = input("Choose a destination from the list: Paris, Lisbon, Milan, Oslo ")
num_nights = int(input("Enter the number of nights for your stay "))
rental_days = int(input("Enter the number of days for your car rental "))

# Function calls to calculate the total cost
total_cost = total_holiday_cost(hotel_cost(num_nights), plane_cost(city_flight), car_rental(rental_days))
print(f"The total cost of your trip to {city_flight} for {num_nights} nights with a {rental_days}-day car rental is £{total_cost}")

Author

Maïa Kalina
Feel free to contribute to the project or provide feedback!
