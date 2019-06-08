import tkinter as tk
from tkinter import ttk
from tkinter import font
import requests

Height = 500
Width = 600

def test_functuion(entry):
	print("This is the entry:",entry)

def formatResponse(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']
		humidity = weather['main']['humidity'] 
		pressure = weather['main']['pressure'] 
		windSpeed = weather['wind']['speed'] 


		finalStr = 'Location:' + str(name) + '\n' '\n' + 'Description:' + str(desc) + '\n' + (
				   'Temperature:' +  str(temp) + '\n' + 
				   'Humidity:' + str(humidity) + '\n' + 
				   'Pressure:' + str(pressure) +'\n' + 
				   'Wind Speed:' + str(windSpeed) )
		# finalStr = 'City: %s \nConditions: \nTemperature (°F): %s' % (name, desc, temp)
	except:
		finalStr = 'There was a problem retriving that information' 
	return finalStr

def getWeather(city):
	weatherKey = "dea3cb8db29bc01683ccfa8a7b6a047a"
	url = "https://api.openweathermap.org/data/2.5/weather"
	params = {'APPID': weatherKey, 'q':city,'units':'imperial'}
	response = requests.get(url,params=params)
	weather = response.json()
	label.configure(text = formatResponse(weather))
	# label['text'] = formatResponse(weather)

root = tk.Tk()
root.configure(background='black')
root.geometry("600x400")
root.title('Weather App')
root.iconbitmap('images/weather.ico')
# root.bind_class('Button', '<Enter>', test)
# root.resizable(1, 1)

style = ttk.Style()
style.configure('TButton', font = ('calibri', 10, 'bold'), foreground = 'red') 
style.configure('TLabel', font = ('calibri', 15, 'italic'), anchor='nw', justify='left',background = '#eaebf7') 
style.configure('TFrame', font = ('calibri', 10, 'italic'), anchor='nw', justify='left',background = '#bbc0f7',foreground="white") 
style.configure('W.TFrame', font = ('calibri', 10, 'italic'), anchor='nw', justify='left')
style.configure('TEntry',foreground='blue')
# canvas = tk.Canvas(root,height=Height,width=Width)
# canvas.pack() 

# background_image = tk.PhotoImage(file="rt.png")
# background_label = tk.Label(root, image=background_image) 
# background_label.place(relwidth=1,relheight=1)

tabControl = ttk.Notebook(root)          # Create Tab Control 

tab1 = ttk.Frame(tabControl)            # Create a tab  
tabControl.add(tab1, text='Current Weather')      # Add the tab 

tab2 = ttk.Frame(tabControl)              
tabControl.add(tab2, text='3hrs Forecast')      # Add a second tab

tab3 = ttk.Frame(tabControl)            
tabControl.add(tab3, text='5 day Forecast')      # Add a third tab 

tabControl.pack(expand=1, fill="both")  # Pack to make tabs visible

frame = ttk.Frame(tab1,style='W.TFrame')
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1, anchor="n")

entry = ttk.Entry(frame,style='TEntry',font=('Arial', 13))
entry.place(relwidth=0.65,relheight=1)

button = ttk.Button(frame,style='TButton', text="Get Weather",command=lambda: getWeather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = ttk.Frame(tab1)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6, anchor="n")


label = ttk.Label(lower_frame,style='TLabel')
label.place(relwidth=1,relheight=1)

# verticalScrollBar = tk.Scrollbar ( lower_frame,orient='vertical')
# verticalScrollBar.pack( side = tk.RIGHT, fill = tk.Y )

# print(getWeather('nairobi'))


# print(tk.font.families())

root.mainloop()