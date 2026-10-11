

# ====================================================================================================================
# You are building a software module for a smart home system. You need to create a Therm class that manages the temperature of a room. To prevent users or other systems from unsafe or unrealistic temperatures, you must hide the raw data and enforce rules throu encapsulation

# Requirements:

# 1. Private Attributes:

# Create a private attribute named_current_temperature (initialize it via the construc

# >Create a private attribute named node (e.g., "Heat", "Cool" , "Off").

# 2. Getter Methods:

# >Create a method get_temperature() that returns the current temperature.

# >Create a method get_mode() that returns the current operational mode.

# 3.Setter Methods with Validation:

# >Create a method set_temperature(temp) that accepts a float/int.

# --Validation rule: The temperature can only be set between 50°F and 90°F (inclusive). 
# If value is outside this range, print an error message: "Error: Temperature must be between and 90 degrees." and do not change the value.

# >Create a method set_mode(mode).

# --Validation rule: The mode must be one of the following: "Heat", "Cool", or "Off". If an d mode is provided, print "Error: Invalid node."
class thermost:
    def __init__(self,current_temperature,moode="off"):
        self.__current_temperature=70
        self.__mode="Off"

        #constructor
        self.set_temperature(current_temperature)
        self.set_mode(moode)

    #getter
    def get_temperature(self):
        return self.__current_temperature

    #mode
    def get_mode(self):
        return self.__mode

    #Setter (Validation)
    def set_temperature(self,temp):
        if 50<=temp<=90:
            self.__current_temperature=temp
        else:
            print('Error: Temperature must be between and 90 degrees')

    #set mode
    def set_mode(self,mode):
        if mode in("Heat", "Cool","Off"):
            self.__mode=mode
        else:
            print('Error: Invalid node.')



# ---------- টেস্ট ----------
t = thermost(72, "Heat")
print("Temperature:", t.get_temperature())
print("Mode:", t.get_mode())

print("\n--- Valid change ---")
t.set_temperature(80)
t.set_mode("Cool")
print("Temperature:", t.get_temperature())
print("Mode:", t.get_mode())

print("\n--- Invalid change ---")
t.set_temperature(120)      # রেঞ্জের বাইরে
t.set_temperature(30)       # রেঞ্জের বাইরে
t.set_mode("Turbo")         # ভুল মোড
print("Temperature:", t.get_temperature())   # আগের মান থাকবে
print("Mode:", t.get_mode())                 # আগের মান থাকবে


print("\n--- Direct access ---")
try:
    print(t.__current_temperature)
except AttributeError:
    print("Error: You cant access private attribute")
        