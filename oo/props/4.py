class SmartLamp:
    def __init__(self, color, brightness):
        self._color = color
        self._brightness = brightness

    def glow(self):
        return (f'The lamp glows {self.color}.')

    @property
    def color(self):                    # Getter for _color
        return self._color

    @color.setter
    def color(self, color):             # Setter for _color
        if not isinstance(color, str):
            raise TypeError('Color must be a color name.')

        self._color = color
    
    @property 
    def brightness(self):
        return self._brightness 
    
    @brightness.setter
    def brightness(self, new_brightness):
        if not isinstance(new_brightness, int):
            raise TypeError("Please input an integer")
        if new_brightness < 0 or new_brightness > 100:
            raise ValueError("Brightness must be between 0 and 100")
        
        self._brightness = new_brightness
        
    def glow(self):
        return f"The lamp glows {self.color} at {self.brightness}%."
    
    
        
lamp = SmartLamp('blue', 70)
print(lamp.color)              # blue
print(lamp.brightness)         # 70
print(lamp.glow())             # The lamp glows blue at 70%.

lamp.color = 'red'
lamp.brightness = 90
print(lamp.color)              # red
print(lamp.brightness)         # 90
print(lamp.glow())             # The lamp glows red at 90%.

lamp.brightness = 120
# ValueError: Brightness must be between 0 and 100.