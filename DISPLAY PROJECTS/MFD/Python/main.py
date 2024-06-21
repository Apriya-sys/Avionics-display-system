import tkinter as tk
import random
import time
from threading import Thread

class MFD:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Function Display (MFD)")
        self.root.configure(bg='black')

        # Creating frames for different sections of the MFD
        self.create_frames()

        # Updating data in the MFD
        self.update_data()

    def create_frames(self):
        # Flight Data Frame
        self.flight_data_frame = tk.Frame(self.root, bg='black', bd=2, relief="ridge")
        self.flight_data_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Engine Monitoring Frame
        self.engine_frame = tk.Frame(self.root, bg='black', bd=2, relief="ridge")
        self.engine_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Navigation Frame
        self.navigation_frame = tk.Frame(self.root, bg='black', bd=2, relief="ridge")
        self.navigation_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Weather Frame
        self.weather_frame = tk.Frame(self.root, bg='black', bd=2, relief="ridge")
        self.weather_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Traffic Frame
        self.traffic_frame = tk.Frame(self.root, bg='black', bd=2, relief="ridge")
        self.traffic_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # Adding labels for flight data
        self.altitude_label = tk.Label(self.flight_data_frame, text="Altitude: 0 ft", fg="cyan", bg="black", font=("Helvetica", 16, "bold"))
        self.altitude_label.pack(expand=True, padx=20, pady=10)
        self.speed_label = tk.Label(self.flight_data_frame, text="Speed: 0 knots", fg="lime", bg="black", font=("Helvetica", 16, "bold"))
        self.speed_label.pack(expand=True, padx=20, pady=10)
        self.heading_label = tk.Label(self.flight_data_frame, text="Heading: N/A", fg="yellow", bg="black", font=("Helvetica", 16, "bold"))
        self.heading_label.pack(expand=True, padx=20, pady=10)

        # Adding labels for engine monitoring
        self.engine_temp_label = tk.Label(self.engine_frame, text="Engine Temp: 0 °C", fg="orange", bg="black", font=("Helvetica", 16, "bold"))
        self.engine_temp_label.pack(expand=True, padx=20, pady=10)
        self.fuel_flow_label = tk.Label(self.engine_frame, text="Fuel Flow: 0 lb/hr", fg="red", bg="black", font=("Helvetica", 16, "bold"))
        self.fuel_flow_label.pack(expand=True, padx=20, pady=10)

        # Adding labels for navigation
        self.navigation_label = tk.Label(self.navigation_frame, text="Navigation Data", fg="yellow", bg="black", font=("Helvetica", 16, "bold"))
        self.navigation_label.pack(expand=True, padx=20, pady=10)

        # Adding labels for weather
        self.weather_label = tk.Label(self.weather_frame, text="Weather: Clear", fg="blue", bg="black", font=("Helvetica", 16, "bold"))
        self.weather_label.pack(expand=True, padx=20, pady=10)

        # Adding labels for traffic
        self.traffic_label = tk.Label(self.traffic_frame, text="Traffic: No Conflict", fg="white", bg="black", font=("Helvetica", 16, "bold"))
        self.traffic_label.pack(expand=True, padx=20, pady=10)

    def update_data(self):
        # Simulating data updates
        def update():
            while True:
                altitude = self.get_altitude()
                speed = self.get_speed()
                heading = self.get_heading()
                engine_temp = self.get_engine_temp()
                fuel_flow = self.get_fuel_flow()
                navigation_data = self.get_navigation_data()
                weather = self.get_weather()
                traffic = self.get_traffic()

                self.altitude_label.config(text=f"Altitude: {altitude:,} ft")
                self.speed_label.config(text=f"Speed: {speed} knots")
                self.heading_label.config(text=f"Heading: {heading}")
                self.engine_temp_label.config(text=f"Engine Temp: {engine_temp} °C")
                self.fuel_flow_label.config(text=f"Fuel Flow: {fuel_flow} lb/hr")
                self.navigation_label.config(text=f"Navigation: {navigation_data}")
                self.weather_label.config(text=f"Weather: {weather}")
                self.traffic_label.config(text=f"Traffic: {traffic}")

                time.sleep(1)  # Update every second

        thread = Thread(target=update)
        thread.daemon = True
        thread.start()

    def get_altitude(self):
        # Placeholder function to simulate altitude data
        return random.randint(1000, 40000)

    def get_speed(self):
        # Placeholder function to simulate speed data
        return random.randint(200, 600)

    def get_heading(self):
        # Placeholder function to simulate heading data
        headings = ["North", "South", "East", "West", "Northeast", "Northwest", "Southeast", "Southwest"]
        return random.choice(headings)

    def get_engine_temp(self):
        # Placeholder function to simulate engine temperature data
        return random.randint(50, 100)

    def get_fuel_flow(self):
        # Placeholder function to simulate fuel flow data
        return random.randint(500, 3000)

    def get_navigation_data(self):
        # Placeholder function to simulate navigation data
        directions = ["Waypoint 1", "Waypoint 2", "Waypoint 3", "Waypoint 4"]
        return random.choice(directions)

    def get_weather(self):
        # Placeholder function to simulate weather data
        weather_conditions = ["Clear", "Cloudy", "Rainy", "Stormy"]
        return random.choice(weather_conditions)

    def get_traffic(self):
        # Placeholder function to simulate traffic data
        traffic_conditions = ["No Conflict", "Traffic Alert", "Collision Warning"]
        return random.choice(traffic_conditions)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x800")
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=2)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    
    mfd = MFD(root)
    root.mainloop()
