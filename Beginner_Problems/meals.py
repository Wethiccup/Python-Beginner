import requests

meal = input("Enter a meal: ")

response = requests.get(f"www.themealdb.com/api/json/v1/1/search.php?s={meal}")
