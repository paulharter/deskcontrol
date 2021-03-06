from tinkerforge.bricklet_temperature import BrickletTemperature
from tinkerforge.bricklet_temperature_ir import BrickletTemperatureIR
from tinkerforge.bricklet_humidity import BrickletHumidity
from tinkerforge.bricklet_voltage_current import BrickletVoltageCurrent
from tinkerforge.bricklet_sound_intensity import BrickletSoundIntensity
from tinkerforge.bricklet_ambient_light_v2 import BrickletAmbientLightV2
from tinkerforge.bricklet_distance_ir import BrickletDistanceIR
from tinkerforge.bricklet_co2 import BrickletCO2
from tinkerforge.bricklet_color import BrickletColor
from tinkerforge.bricklet_barometer import BrickletBarometer
from tinkerforge.bricklet_line import BrickletLine
from tinkerforge.bricklet_hall_effect import BrickletHallEffect
from tinkerforge.bricklet_accelerometer import BrickletAccelerometer
from tinkerforge.bricklet_moisture import BrickletMoisture
from tinkerforge.bricklet_dual_relay import BrickletDualRelay
from tinkerforge.bricklet_motion_detector import BrickletMotionDetector

SENSORS = {
    "temp": {
        "name": "Temperature",
        "class": BrickletTemperature,
        "units": "degC",
        "brick_tag": "Temperature_Sensor",
        "value_func": "get_temperature",
        "multiplier": 0.01,
        "callback_func": "CALLBACK_TEMPERATURE",
    },
    "irtemp": {
        "name": "IR Temperature",
        "class": BrickletTemperatureIR,
        "units": "degC",
        "brick_tag": "IRTemperature_Sensor",
        "value_func": "get_object_temperature",
        "multiplier": 0.1,
        "callback_func": "CALLBACK_OBJECT_TEMPERATURE",
    },
    "humidity": {
        "name": "Humidity",
        "class": BrickletHumidity,
        "units": "%RH",
        "brick_tag": "Humidity_Sensor",
        "value_func": "get_humidity",
        "multiplier": 0.1,
        "callback_func": "CALLBACK_HUMIDITY",
    },
    "light": {
        "name": "Ambient Light",
        "class": BrickletAmbientLightV2,
        "units": "lux",
        "brick_tag": "LightingSystem_Illuminance_Sensor",
        "value_func": "get_illuminance",
        "multiplier": 0.01,
        "callback_func": "CALLBACK_ILLUMINANCE",
    },
    "sound": {
        "name": "Sound Intensity",
        "class": BrickletSoundIntensity,
        "units": "",
        "brick_tag": "Noise_Sensor",
        "value_func": "get_intensity",
        "callback_func": "CALLBACK_INTENSITY",
    },
    "co2": {
        "name": "Carbon Dioxide",
        "class": BrickletCO2,
        "units": "ppm",
        "brick_tag": "CO2_Sensor",
        "value_func": "get_co2_concentration",
        "callback_func": "CALLBACK_CO2_CONCENTRATION",
    },
    "voltage": {
        "name": "Voltage",
        "class": BrickletVoltageCurrent,
        "units": "V",
        "brick_tag": "Electrical_Power_Meter",
        "value_func": "get_voltage",
        "multiplier": 0.01,
        "value_offset": 0,
        "callback_func": "CALLBACK_VOLTAGE",
    },
    "current": {
        "name": "Current",
        "class": BrickletVoltageCurrent,
        "units": "A",
        "brick_tag": "Electrical_Power_Meter",
        "value_func": "get_current",
        "multiplier": 0.01,
        "callback_func": "CALLBACK_CURRENT",
    },
    "power": {
        "name": "Power",
        "class": BrickletVoltageCurrent,
        "units": "W",
        "brick_tag": "Electrical_Power_Meter",
        "value_func": "get_power",
        "multiplier": 0.01,
        "callback_func": "CALLBACK_POWER",
    },
    "dist": {
        "name": "Desk Height",
        "class": BrickletDistanceIR,
        "units": "cm",
        "brick_tag": "Range_Sensor",
        "value_func": "get_distance",
        "multiplier": 0.1,
        "callback_func": "CALLBACK_DISTANCE",
    },
    "colour_temp": {
        "name": "Colour Temp",
        "class": BrickletColor,
        "units": "K",
        "brick_tag": "Colour_Temperature_Sensor",
        "value_func": "get_color",
        "callback_func": "CALLBACK_COLOR",
    },
    "air_pressure": {
        "name": "Air Pressure",
        "class": BrickletBarometer,
        "units": "mbar",
        "brick_tag": "Air_Pressure_Sensor",
        "value_func": "get_air_pressure",
        "multiplier": 0.001,
        "callback_func": "CALLBACK_AIR_PRESSURE",
    },
    "reflectivity": {
        "name": "Reflectivity",
        "class": BrickletLine,
        "units": "",
        "brick_tag": "Line_Sensor",
        "value_func": "get_reflectivity",
        "callback_func": "CALLBACK_REFLECTIVITY",
    },
    "magfield": {
        "name": "Magn. Field",
        "class": BrickletHallEffect,
        "units": "",
        "brick_tag": "Magnetic_Field_Sensor",
        "value_func": "get_edge_count",
        "callback_func": "CALLBACK_EDGE_COUNT",
    },
    "acceleration": {
        "name": "Vibration",
        "class": BrickletAccelerometer,
        "units": "g",
        "brick_tag": "Accelerometer_Sensor",
        "value_func": "get_acceleration",
        "multiplier": 0.001,
        "callback_func": "CALLBACK_ACCELERATION",
    },
    "moisture": {
        "name": "Moisture",
        "class": BrickletMoisture,
        "units": "",
        "brick_tag": "Moisture_Sensor",
        "value_func": "get_moisture_value",
        "callback_func": "CALLBACK_MOISTURE",
    },
    "relay_a": {
        "name": "Relay Channel 1",
        "class": BrickletDualRelay,
        "units": "",
        "brick_tag": "Relay_Sensor",
        "value_func": "get_state",
    },
    "relay_b": {
        "name": "Relay Channel 2",
        "class": BrickletDualRelay,
        "units": "",
        "brick_tag": "Relay_Sensor",
        "value_func": "get_state",
    },
    "motion": {
        "name": "Motion Detector",
        "class": BrickletMotionDetector,
        "units": "",
        "brick_tag": "Motion_Detector",
        "value_func": "get_motion_detected",
    },
}
