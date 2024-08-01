# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:27:38 2024

@author: User
"""
import matplotlib.pyplot as plt

def calculate_aqi(pollutant_concentration):
    
    pm25_concentration = 45

    aqi_pm25 = calculate_aqi(pm25_concentration)

    print(f"AQI for PM2.5: {aqi_pm25}")
    
    return aqi_pm25

def calculate_noise_level(sound_pressure_levels):
    
    sound_pressure_levels = [80, 85, 90]

    noise_level = calculate_noise_level(sound_pressure_levels)

    print(f"Noise Pollution Level: {noise_level} dB")
    
    return noise_level

def calculate_wqi(water_parameters):
    
    water_parameters = {"pH": input(float("Enter pH value=")), "DO": input(float("Enter DO=")), "BOD":input(float("Enter BOD="))}

    wqi_parameters = calculate_wqi(water_parameters)
    
    print(f"Water Quality Index: {wqi_parameters}")
    
    return wqi_parameters
    
user_pm25_concentration = float(input("Enter PM2.5 concentration:"))

user_sound_pressure_levels = [float(level) for level in input ("Enter sound pressure levels (comma-separated dB values):")]

user_water_parameters = {"pH": float(input("Enter pH:")), "DO": float(input("Enter DO=")), "BOD":float(input("Enter BOD="))}
    
user_aqi_pm25 = calculate_aqi(user_pm25_concentration)

user_noise_level = calculate_noise_level(user_sound_pressure_levels)

user_wqi_water = calculate_wqi(user_water_parameters)

print(f"AQI for PM2.5: {user_aqi_pm25}\nNoise Pollution Level: {user_noise_level} dB\nWater Quality Index: {user_wqi_water}")


    