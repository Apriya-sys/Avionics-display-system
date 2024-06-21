import tkinter as tk
from tkinter import ttk
import random
import time
from threading import Thread

class FMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Management System (FMS)")
        self.root.geometry("1200x800")
        self.root.configure(bg='black')
        self.create_widgets()
        self.update_data()

    def create_widgets(self):
        # Configure grid layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Flight Plan Frame
        self.flight_plan_frame = tk.Frame(self.root, bg='black', bd=2, relief="ridge")
        self.flight_plan_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.flight_plan_label = tk.Label(self.flight_plan_frame, text="Flight Plan", fg="white", bg="black", font=("Helvetica", 16, "bold"))
        self.flight_plan_label.pack(pady=10)

        self.waypoints_listbox = tk.Listbox(self.flight_plan_frame, bg='black', fg='white', font=("Helvetica", 12))
        self.waypoints_listbox.pack(expand=True, fill="both", padx=20, pady=10)

        # Navigation Frame
        self.navigation_frame = tk.Frame(self.root, bg='black', bd=2, relief="ridge")
        self.navigation_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.navigation_label = tk.Label(self.navigation_frame, text="Navigation Data", fg="white", bg="black", font=("Helvetica", 16, "bold"))
        self.navigation_label.pack(pady=10)

        self.nav_data_text = tk.Text(self.navigation_frame, bg='black', fg='white', font=("Helvetica", 12), wrap="none")
        self.nav_data_text.pack(expand=True, fill="both", padx=20, pady=10)
        self.nav_scrollbar = ttk.Scrollbar(self.navigation_frame, command=self.nav_data_text.yview)
        self.nav_scrollbar.pack(side="right", fill="y")
        self.nav_data_text.config(yscrollcommand=self.nav_scrollbar.set)

        # Performance Frame
        self.performance_frame = tk.Frame(self.root, bg='black', bd=2, relief="ridge")
        self.performance_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

        self.performance_label = tk.Label(self.performance_frame, text="Performance Data", fg="white", bg="black", font=("Helvetica", 16, "bold"))
        self.performance_label.pack(pady=10)

        self.perf_data_text = tk.Text(self.performance_frame, bg='black', fg='white', font=("Helvetica", 12), wrap="none")
        self.perf_data_text.pack(expand=True, fill="both", padx=20, pady=10)
        self.perf_scrollbar = ttk.Scrollbar(self.performance_frame, command=self.perf_data_text.yview)
        self.perf_scrollbar.pack(side="right", fill="y")
        self.perf_data_text.config(yscrollcommand=self.perf_scrollbar.set)

        # Weather Frame
        self.weather_frame = tk.Frame(self.root, bg='black', bd=2, relief="ridge")
        self.weather_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.weather_label = tk.Label(self.weather_frame, text="Weather Data", fg="white", bg="black", font=("Helvetica", 16, "bold"))
        self.weather_label.pack(pady=10)

        self.weather_data_text = tk.Text(self.weather_frame, bg='black', fg='white', font=("Helvetica", 12), wrap="none")
        self.weather_data_text.pack(expand=True, fill="both", padx=20, pady=10)
        self.weather_scrollbar = ttk.Scrollbar(self.weather_frame, command=self.weather_data_text.yview)
        self.weather_scrollbar.pack(side="right", fill="y")
        self.weather_data_text.config(yscrollcommand=self.weather_scrollbar.set)

        # Traffic Frame
        self.traffic_frame = tk.Frame(self.root, bg='black', bd=2, relief="ridge")
        self.traffic_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.traffic_label = tk.Label(self.traffic_frame, text="Traffic Information", fg="white", bg="black", font=("Helvetica", 16, "bold"))
        self.traffic_label.pack(pady=10)

        self.traffic_data_text = tk.Text(self.traffic_frame, bg='black', fg='white', font=("Helvetica", 12), wrap="none")
        self.traffic_data_text.pack(expand=True, fill="both", padx=20, pady=10)
        self.traffic_scrollbar = ttk.Scrollbar(self.traffic_frame, command=self.traffic_data_text.yview)
        self.traffic_scrollbar.pack(side="right", fill="y")
        self.traffic_data_text.config(yscrollcommand=self.traffic_scrollbar.set)

        # Adding initial data
        self.init_flight_plan()
        self.init_navigation_data()
        self.init_performance_data()
        self.init_weather_data()
        self.init_traffic_data()

    def init_flight_plan(self):
        self.waypoints = ["WAYPOINT1", "WAYPOINT2", "WAYPOINT3", "WAYPOINT4"]
        for waypoint in self.waypoints:
            self.waypoints_listbox.insert(tk.END, waypoint)

    def init_navigation_data(self):
        nav_data = (
            "Current Position: LAT 37.7749° N, LONG 122.4194° W\n"
            "Next Waypoint: WAYPOINT2\n"
            "Distance to Next Waypoint: 150 NM\n"
            "Estimated Time of Arrival: 12:34 UTC"
        )
        self.nav_data_text.insert(tk.END, nav_data)

    def init_performance_data(self):
        perf_data = (
            "Current Airspeed: 450 knots\n"
            "Current Altitude: 35,000 ft\n"
            "Fuel Remaining: 12,000 lbs\n"
            "Estimated Fuel at Destination: 6,500 lbs\n"
            "Gross Weight: 150,000 lbs\n"
            "Temperature: -40°C"
        )
        self.perf_data_text.insert(tk.END, perf_data)

    def init_weather_data(self):
        weather_data = (
            "Current Weather: Clear\n"
            "Wind: 270° at 15 knots\n"
            "Temperature: 20°C\n"
            "Visibility: 10 miles"
        )
        self.weather_data_text.insert(tk.END, weather_data)

    def init_traffic_data(self):
        traffic_data = (
            "Traffic: No Conflict\n"
            "Nearest Aircraft: 5 NM\n"
            "TCAS Status: Normal"
        )
        self.traffic_data_text.insert(tk.END, traffic_data)

    def update_data(self):
        def update():
            while True:
                # Simulate dynamic data updates
                new_speed = random.randint(440, 460)
                new_altitude = random.randint(34000, 36000)
                new_fuel = random.randint(11500, 12500)
                nav_position = f"Current Position: LAT {round(random.uniform(30, 50), 4)}° N, LONG {round(random.uniform(-130, -70), 4)}° W"

                perf_data = (
                    f"Current Airspeed: {new_speed} knots\n"
                    f"Current Altitude: {new_altitude} ft\n"
                    f"Fuel Remaining: {new_fuel} lbs\n"
                    "Estimated Fuel at Destination: 6,500 lbs\n"
                    "Gross Weight: 150,000 lbs\n"
                    "Temperature: -40°C"
                )
                
                nav_data = (
                    f"{nav_position}\n"
                    "Next Waypoint: WAYPOINT2\n"
                    "Distance to Next Waypoint: 150 NM\n"
                    "Estimated Time of Arrival: 12:34 UTC"
                )

                weather_data = (
                    f"Current Weather: {random.choice(['Clear', 'Cloudy', 'Rainy', 'Stormy'])}\n"
                    f"Wind: {random.randint(0, 360)}° at {random.randint(0, 30)} knots\n"
                    f"Temperature: {random.randint(-40, 40)}°C\n"
                    "Visibility: 10 miles"
                )

                traffic_data = (
                    f"Traffic: {random.choice(['No Conflict', 'Traffic Alert', 'Collision Warning'])}\n"
                    f"Nearest Aircraft: {random.randint(1, 10)} NM\n"
                    "TCAS Status: Normal"
                )

                self.perf_data_text.delete(1.0, tk.END)
                self.perf_data_text.insert(tk.END, perf_data)
                
                self.nav_data_text.delete(1.0, tk.END)
                self.nav_data_text.insert(tk.END, nav_data)
                
                self.weather_data_text.delete(1.0, tk.END)
                self.weather_data_text.insert(tk.END, weather_data)
                
                self.traffic_data_text.delete(1.0, tk.END)
                self.traffic_data_text.insert(tk.END, traffic_data)

                time.sleep(5)

        thread = Thread(target=update)
        thread.daemon = True
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = FMS(root)
    root.mainloop()
