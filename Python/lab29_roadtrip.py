

city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

user_city_choice = input('Enter your starting city, either: Boston, New York, Albany, Portland or Philadelphia: ')

print(str(city_to_accessible_cities[user_city_choice]) + ' are the closest cities from your starting point')