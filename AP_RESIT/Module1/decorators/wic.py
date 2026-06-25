def sensor_output(sensor_name, unit):
    # TODO:
    # This decorator has parameters, so you need 3 layers.
    def wrapper1(func):
        def wrapper2(*args, **kwargs):
            
            numbs = func(*args, **kwargs) # unit, args, kwargs
            if type(numbs) != float:
                raise ValueError("Invalid Sensor reading")
            numbs =  round(numbs,2)
            return (sensor_name, numbs, unit)
        return wrapper2
    return wrapper1
    


@sensor_output("Temperature", "C")
def read_temperature(raw_value, offset=0):
    return raw_value + offset


@sensor_output("Pressure", "kPa")
def read_pressure(raw_value):
    return raw_value / 1000


@sensor_output("Humidity", "%")
def read_humidity(raw_value):
    return raw_value


print(read_temperature(21.678, offset=0.5))
print(read_pressure(101325))
print(read_humidity(55.555))

#Uncomment to test error handling:
#print(read_humidity("high"))