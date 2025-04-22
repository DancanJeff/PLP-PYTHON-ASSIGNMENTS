class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.powered_on = False
    
    def power_toggle(self):
        self.powered_on = not self.powered_on
        status = "on" if self.powered_on else "off"
        return f"{self.brand} {self.model} is now {status}"

class Smartphone(Device):
    def __init__(self, brand, model, screen_size, storage):
        super().__init__(brand, model)
        self.screen_size = screen_size
        self.storage = storage
        self.apps = []
        self.battery = 100
    
    def install_app(self, app_name):
        if app_name not in self.apps:
            self.apps.append(app_name)
            return f"{app_name} installed successfully"
        return f"{app_name} is already installed"
    
    def charge_battery(self, amount):
        self.battery = min(100, self.battery + amount)
        return f"Battery level: {self.battery}%"
    
    def get_info(self):
        return f"""
Brand: {self.brand}
Model: {self.model}
Screen Size: {self.screen_size} inches
Storage: {self.storage}GB
Battery: {self.battery}%
Apps Installed: {', '.join(self.apps) if self.apps else 'None'}
"""

# Example usage
if __name__ == "__main__":
    # Create a new smartphone
    my_phone = Smartphone("Samsung", "Galaxy S21", 6.2, 128)
    
    # Test the functionality
    print(my_phone.power_toggle())
    print(my_phone.install_app("WhatsApp"))
    print(my_phone.install_app("Instagram"))
    print(my_phone.charge_battery(20))
    print(my_phone.get_info())