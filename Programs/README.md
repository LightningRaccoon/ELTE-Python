# Home Automation System Documentation
`by Regő Székely (H5LJFS)`

# Classes
### 'IoTDevice' Class
- **Attributes**:
  - `device_id (str)`: Identifier for the IoT device.
  - `device_name (str)`: Name of the IoT device.
  - `status (bool)`: Status of the IoT device (On/Off).
- **Methods**:
    - `toggle_status()`: Toggles the status of the IoT device.

### SmartLight Class (Inherits from IoTDevice)
- **Attributes**:
    - `brightness (int)`: Brightness level of the smart light.
- **Methods**:
    - `set_brightness(brightness: int)`: Sets the brightness level of the smart light.
    - `random_brightness()`: Sets a random brightness level for the smart light.
### Thermostat Class (Inherits from IoTDevice)
- **Attributes**:
    - `temperature (int)`: Temperature set on the thermostat.
- **Methods**:
    - `set_temperature(temperature: int)`: Sets the temperature on the thermostat.
    - `random_temperature()`: Sets a random temperature on the thermostat.
### SecurityCamera Class (Inherits from IoTDevice)
- **Attributes**:
    - `motion_detected (bool)`: Indicates whether motion is detected.
- **Methods**:
    - `change_motion()`: Changes the motion detection status.
### AutomationSystem Class
- **Attributes**:
    - `name (str)`: Name of the automation system.
    - `devices (list)`: List of IoT devices in the system.
    - `randomization_enabled (bool)`: Indicates whether randomization is enabled for the system.
- **Methods**:
    - `add_device(device: IoTDevice)`: Adds an IoT device to the system.
    - `find_device(device_id: str)`: Finds an IoT device by its ID.
    - `perform_auto_task()`: Performs an automated task on all devices in the system.
    - `simulation_cycle(dashboard: Dashboard, interval_seconds: int = 1)`: Simulates a cycle of automated tasks.
### Dashboard Class
- **Attributes**:
    - `root (customtkinter.CTk())`: The main window of the GUI.
    - `system (AutomationSystem)`: The automation system associated with the dashboard.
    - `labels (list)`: List to store label information.
    - `automation_on (bool)`: Indicates whether automation is currently on.
    - `aut_button_text (customtkinter.StringVar)`: Text variable for the automation button.
- **Methods**:
    - `toggle_automation()`: Toggles the automation status and simulates automated tasks.
    - `toggle_on_off(device: IoTDevice)`: Toggles the status of an IoT device.
    - `update_values()`: Updates the values displayed in the dashboard.
    - `create_device_controls()`: Creates controls for each device in the system.
    - `__create_light_control(light: SmartLight)`: Creates controls specific to smart lights.
    - `__dashb_set_brightness(light: SmartLight, brightness: int)`: Sets the brightness of a smart light.
    - `__create_thermostat_control(thermostat: Thermostat)`: Creates controls specific to thermostats.
    - `__dashb_set_temperature(thermostat: Thermostat, temperature: int)`: Sets the temperature of a thermostat.
    - `__create_security_camera_control(security_camera: SecurityCamera)`: Creates controls specific to security cameras.
    - `__dashb_change_motion(security_camera: SecurityCamera)`: Changes the motion detection status of a security camera.

### Instructions to Run the Code:
- Ensure that you have Python installed on your system.
- Execute the Python script in an environment that supports **customtkinter** (the GUI library used in the code).
- The GUI window will appear, displaying the home automation system dashboard.
- Interact with the controls to toggle device status, set brightness/temperature, and simulate automation tasks.
### Testing:
Test Case 1: Toggle Device Status
- Steps:
    - Open the GUI.
    - Click the "Toggle On/Off" button for a smart light or thermostat.
- Expected Result:
    - The status of the respective device should toggle between "On" and "Off" in the GUI.


Test Case 2: Set Brightness/Temperature
- Steps:
    - Open the GUI.
    - Adjust the brightness slider for a smart light or the temperature slider for a thermostat.
- Expected Result:
    - The brightness/temperature of the respective device should update in the GUI.

Test Case 3: Simulate Automation Tasks
- Steps:
    - Open the GUI.
    - Click the "Automation random" button to toggle automation.
- Expected Result:
    - If automation is turned on, the system should perform random tasks for a set number of simulation cycles.
    - The GUI should display the updated values of devices.

>**Note**: Due to GUI update timing, only the last updated values will be seen in the GUI. But the simulation runs and writes every steps to the command line. 

>**Note**: Make sure to use the customtkinter v5.2.0 or older because the newest version has an internal bug!


## Packages

This program is using the **customtkinter** package which is originated from the Tkinter package.

| Package | Page | Owner |
| ------ | ------ | ------ |
| customtkinter | https://customtkinter.tomschimansky.com | Tom Schimansky |



