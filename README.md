# DISPLAY-PRJOECTS

This repository contains implementations of an Avionics Display System in both Python and Java. The system provides essential flight information to pilots, enhancing situational awareness and safety.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Avionics Display System is designed to present critical flight data such as altitude, speed, heading, engine parameters, navigation data, weather conditions, and traffic alerts. Implementations are provided in both Python (using Tkinter) and Java (using JavaFX).

## Features

### Python Implementation (Tkinter)
- **Flight Data**: Altitude, speed, and heading.
- **Engine Monitoring**: Engine temperature and fuel flow.
- **Navigation Data**: Current position, next waypoint, distance to waypoint, and ETA.
- **Weather Information**: Current weather conditions.
- **Traffic Information**: Traffic alerts and nearest aircraft.

### Java Implementation (JavaFX)
- **Real-Time Updates**: Data refreshed every few seconds.
- **Organized Layout**: Structured display using GridPane.
- **Custom Styling**: Consistent UI elements for a professional look.
- **Modular Design**: Separate frames for flight data, engine monitoring, navigation, weather, and traffic information.

## Technologies

- **Python**: Tkinter
- **Java**: JavaFX

## Installation

### Python

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/DISPLAY-PROJECTS.git
    cd DISPLAY-PROJECTS/python
    ```

2. **Install Required Packages**:
    ```sh
    pip install tkinter
    ```

3. **Run the Application**:
    ```sh
    python fms.py
    ```

### Java

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/Msreevalli/DISPLAY-PROJECTS.git
    cd DISPLAY-PROJECTS/java
    ```

2. **Download and Setup JavaFX**:
    - Download the JavaFX SDK from [Gluon](https://gluonhq.com/products/javafx/).
    - Extract the SDK and set the `PATH_TO_FX` environment variable to the `lib` directory of the extracted SDK.

3. **Compile and Run the Application**:
    ```sh
    javac --module-path $PATH_TO_FX --add-modules javafx.controls,javafx.fxml FMSDisplay.java
    java --module-path $PATH_TO_FX --add-modules javafx.controls,javafx.fxml FMSDisplay
    ```

## Usage

### Python

Run the Python script to start the Avionics Display System. The GUI will display real-time updates of flight data, engine monitoring, navigation data, weather information, and traffic alerts.

### Java

Compile and run the Java application to start the Avionics Display System. The system will provide a similar display and real-time updates as the Python version, leveraging JavaFX for a robust and scalable implementation.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

