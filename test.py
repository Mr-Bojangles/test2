import requests


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://arstechnica.com")
print(r.status_code)

name = input("Your name: ")
print("Hello,", name)
