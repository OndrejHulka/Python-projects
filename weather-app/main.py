from tkinter import *
import requests


def search():


    api_key = ""
    city = entry_bar.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    data = response
    try:
        city = data['name']
    except KeyError:
        city_label.config(text="This city does not exist")

    city_final = data['name']
    country = data['sys']['country']
    temp = float(data['main']['temp'])-273.15
    min = round(float(data['main']['temp_min']) - 273.15)
    max = round(float(data['main']['temp_max']) - 273.15)
    feel = round(float(data['main']['feels_like']) - 273.15)

    city_label.config(text=f"{city_final}, {country}")

    temp = round(float(data['main']['temp']) - 273.15)
    sky = data['weather'][0]['description']

    tempetature.config(text=f"{temp}°c")
    sky_label.config(text=f"{sky}")
    min_max_feel.config(text=f"minimal tempetature: {min}                 maximal tempetature: {max}                feeling tempetature:{feel}")

    icon = data['weather'][0]['icon']

    entry_bar.delete(0, END)

    image_set(icon)


def image_set(icon):
    if icon == "01d":
        image.config(file="01d.png")
    elif icon == "01n":
        image.config(file="01n.png")
    elif icon == "02d":
        image.config(file="02d.png")
    elif icon == "02n":
        image.config(file="02n.png")
    elif icon == "03d":
        image.config(file="03d.png")
    elif icon == "03n":
        image.config(file="03n.png")
    elif icon == "04d":
        image.config(file="04d.png")
    elif icon == "04n":
        image.config(file="04n.png")
    elif icon == "09d":
        image.config(file="09d.png")
    elif icon == "09n":
        image.config(file="09n.png")
    elif icon == "10d":
        image.config(file="10d.png")
    elif icon == "10n":
        image.config(file="10n.png")
    elif icon == "11d":
        image.config(file="11d.png")
    elif icon == "11n":
        image.config(file="11n.png")
    elif icon == "13d":
        image.config(file="13d.png")
    elif icon == "13n":
        image.config(file="13n.png")
    elif icon == "50d":
        image.config(file="50d.png")
    elif icon == "50n":
        image.config(file="50n.png")

def error(data, city):
    try:
        city = data
    except KeyError:
        city_label.config(text="This city doesnt exist")


window = Tk()
window.geometry('700x350')
window.title("Weather app")
window.resizable(False, False)

#labels
entry_bar = Entry(window, width=30, font=("Libre Baskerville", 15), justify="center")
entry_bar.pack(pady=5)

btn_search = Button(window, width=15, text="Search weather", font=("Arial", 12), command=search)
btn_search.pack()

city_label = Label(window, font=("Libre Baskerville", 21))
city_label.pack(pady=10)

image = PhotoImage()

image_label = Label(window, image=image)
image_label.pack()

sky_label = Label(window, font=("Libre Baskerville", 12))
sky_label.pack()

tempetature = Label(window, font=("Libre Baserville", 21))
tempetature.pack()

min_max_feel = Label(window, font=("Libre Baskerville", 10))
min_max_feel.pack()

window.mainloop()


