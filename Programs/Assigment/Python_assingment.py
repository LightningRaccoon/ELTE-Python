import random
import time
import customtkinter


class IoTDevice:
    def __init__(self, device_id, device_name):
        self.device_id = device_id
        self.device_name = device_name
        self.status = False

    def toggle_status(self):
        self.status = not self.status


class SmartLight(IoTDevice):
    def __init__(self, device_id, device_name, brightness):
        super().__init__(device_id, device_name)
        self.brightness = brightness

    def set_brightness(self, brightness):
        self.brightness = brightness

    def random_brightness(self):
        self.brightness = random.randint(0, 100)


class Thermostat(IoTDevice):
    def __init__(self, device_id, device_name, temperature):
        super().__init__(device_id, device_name)
        self.temperature = temperature

    def set_temperature(self, temperature):
        self.temperature = temperature

    def random_temperature(self):
        self.temperature = random.randint(0, 30)


class SecurityCamera(IoTDevice):
    def __init__(self, device_id, device_name, motion_detected):
        super().__init__(device_id, device_name)
        self.motion_detected = motion_detected

    def change_motion(self):
        self.motion_detected = not self.motion_detected


class Dashboard:
    def __init__(self, root, system):
        super().__init__()
        self.root = root
        self.system = system

        self.root.title("Home Automation System")
        self.root.geometry("600x230")
        self.root.minsize(600, 230)
        self.root.maxsize(600, 230)
        self.root.grid_columnconfigure((0), weight=1)

        self.labels = []
        self.automation_on = False

        self.aut_button_text = customtkinter.StringVar()
        self.aut_button_text.set("Automation random")
        self.automation_button = customtkinter.CTkButton(root, textvariable=self.aut_button_text,
                                                         command=self.toggle_automation)
        self.automation_button.grid(row=4, column=0, padx=20, pady=20, sticky="ew", columnspan=4)

        self.create_device_controls()
        self.update_values()

    def toggle_automation(self):
        self.automation_on = not self.automation_on
        if self.automation_on:
            self.system.randomization_enabled = True

            i = 0
            while i < 10:
                self.system.perform_auto_task()
                print("Simulation cycle: {}".format(i))
                print("Light brightness: {}".format(self.system.find_device("light001").brightness))
                print("Thermostat temperature: {}".format(self.system.find_device("thermostat001").temperature))
                print("Security camera motion: {}".format(self.system.find_device("camera001").motion_detected))
                print()
                time.sleep(1)
                i += 1
                self.update_values()

            # self.system.simulation_cycle(self)
        else:
            self.system.randomization_enabled = False
        self.automation_on = not self.automation_on
        self.aut_button_text.set("Automation random: {}".format("ON" if self.automation_on else "OFF"))

    def toggle_on_off(self, device):
        device.toggle_status()
        self.update_values()

    def update_values(self):
        for label_info in self.labels:
            device = label_info['device']
            label_variable = label_info['label']
            status = "On" if device.status else "Off"

            if isinstance(device, SmartLight):
                label_variable.set(f"Brightness: {device.brightness} - Status: {status}")
            elif isinstance(device, Thermostat):
                label_variable.set(f"Temperature: {device.temperature} - Status: {status}")
            elif isinstance(device, SecurityCamera):
                label_variable.set(f"Motion: {device.motion_detected} - Status: {status}")

        self.root.after(1000, self.update_values)

    def create_device_controls(self):
        for device in self.system.devices:
            if isinstance(device, SmartLight):
                self.__create_light_control(device)
            elif isinstance(device, Thermostat):
                self.__create_thermostat_control(device)
            elif isinstance(device, SecurityCamera):
                self.__create_security_camera_control(device)

    def __create_light_control(self, light):
        label = customtkinter.CTkLabel(root,
                                       text=f"{light.device_name}",
                                       anchor="w",
                                       width=100, height=50,
                                       padx=0, pady=20)
        label.grid(row=len(self.labels), column=0)

        brightness_slider = customtkinter.CTkSlider(root,
                                                    from_=0, to=100,
                                                    command=lambda value, templight=light: self.__dashb_set_brightness(
                                                        templight, value),
                                                    width=150)
        brightness_slider.set(light.brightness)
        brightness_slider.grid(row=len(self.labels), column=1)

        toggle_button = customtkinter.CTkButton(root,
                                                text="Toggle On/Off",
                                                command=lambda tempdevice=light: self.toggle_on_off(tempdevice),
                                                width=100, height=30)
        toggle_button.grid(row=len(self.labels), column=2)

        self.labels.append({
            'id': light.device_id,
            'label': customtkinter.StringVar(),
            'device': light
        })

        name_label = customtkinter.CTkLabel(root,
                                            textvariable=self.labels[len(self.labels) - 1]['label'],
                                            anchor="e",
                                            width=100, height=50,
                                            padx=10, pady=20)
        name_label.grid(row=len(self.labels) - 1, column=3)

    def __dashb_set_brightness(self, light, brightness):
        light.set_brightness(int(brightness))
        self.update_values()

    def __create_thermostat_control(self, thermostat):
        label = customtkinter.CTkLabel(root,
                                       text=f"{thermostat.device_name}",
                                       anchor="w",
                                       width=100, height=50,
                                       padx=0, pady=20)
        label.grid(row=len(self.labels), column=0)

        temperature_slider = customtkinter.CTkSlider(root,
                                                     from_=10, to=30,
                                                     command=lambda value, tempthermostat=thermostat: self.__dashb_set_temperature(tempthermostat, value),
                                                     width=150)
        temperature_slider.set(thermostat.temperature)
        temperature_slider.grid(row=len(self.labels), column=1)

        toggle_button = customtkinter.CTkButton(root,
                                                text="Toggle On/Off",
                                                command=lambda tempdevice=thermostat: self.toggle_on_off(tempdevice),
                                                width=100, height=30)
        toggle_button.grid(row=len(self.labels), column=2)

        self.labels.append({
            'id': thermostat.device_id,
            'label': customtkinter.StringVar(),
            'device': thermostat
        })
        name_label = customtkinter.CTkLabel(root,
                                            textvariable=self.labels[len(self.labels) - 1]['label'],
                                            anchor="w",
                                            width=100, height=50,
                                            padx=10, pady=20)
        name_label.grid(row=len(self.labels) - 1, column=3)

    def __dashb_set_temperature(self, thermostat, temperature):
        thermostat.set_temperature(int(temperature))
        self.update_values()

    def __create_security_camera_control(self, security_camera):
        label = customtkinter.CTkLabel(root,
                                       text=f"{security_camera.device_name}",
                                       anchor="w",
                                       width=100, height=50,
                                       padx=0, pady=20)
        label.grid(row=len(self.labels), column=0)

        change_button = customtkinter.CTkButton(root, text="Change Motion",
                                                command=lambda tempcamera=security_camera: self.__dashb_change_motion(
                                                    tempcamera),
                                                width=100)
        change_button.grid(row=len(self.labels), column=1)

        toggle_button = customtkinter.CTkButton(root, text="Toggle On/Off",
                                                command=lambda tempdevice=security_camera: self.toggle_on_off(
                                                    tempdevice),
                                                width=100, height=30)
        toggle_button.grid(row=len(self.labels), column=2)

        self.labels.append({
            'id': security_camera.device_id,
            'label': customtkinter.StringVar(),
            'device': security_camera
        })

        name_label = customtkinter.CTkLabel(root,
                                            textvariable=self.labels[len(self.labels) - 1]['label'],
                                            anchor="w",
                                            width=150, height=50,
                                            padx=10, pady=20)
        name_label.grid(row=len(self.labels) - 1, column=3)

    def __dashb_change_motion(self, security_camera):
        security_camera.change_motion()
        self.update_values()


class AutomationSystem:
    def __init__(self, name):
        self.name = name
        self.devices = []
        self.randomization_enabled = False

    def add_device(self, device):
        self.devices.append(device)

    def find_device(self, device_id):
        for device in self.devices:
            if device.device_id == device_id:
                return device
        return None

    def perform_auto_task(self):
        for device in self.devices:
            if isinstance(device, SmartLight):
                device.random_brightness()
            elif isinstance(device, Thermostat):
                device.random_temperature()
            elif isinstance(device, SecurityCamera):
                device.change_motion()

    def simulation_cycle(self, dashboard, interval_seconds=1):
        i = 0
        while i < 10:
            self.perform_auto_task()
            print("Simulation cycle: {}".format(i))
            print("Light brightness: {}".format(self.find_device("light001").brightness))
            print("Thermostat temperature: {}".format(self.find_device("thermostat001").temperature))
            print("Security camera motion: {}".format(self.find_device("camera001").motion_detected))
            print()
            time.sleep(interval_seconds)
            i += 1
            dashboard.update_values()


root = customtkinter.CTk()
root.title("Home Automation System")
automation_system = AutomationSystem("Home Automation System")
light = SmartLight("light001", "Living Room Light", 0)
thermostat = Thermostat("thermostat001", "Living Room Thermostat", 10)
security_camera = SecurityCamera("camera001", "Living Room Camera", False)

automation_system.add_device(light)
automation_system.add_device(thermostat)
automation_system.add_device(security_camera)

d = Dashboard(root, automation_system)

root.mainloop()
