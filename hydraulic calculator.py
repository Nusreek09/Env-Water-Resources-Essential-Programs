# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:27:36 2024

@author: User
"""

#the following is a python project to create a hydraulic calculator

import math

def calculate_flow_rate(area,velocity):
    return (area*velocity)

pipe_area= float(input("Enter your pipe area="))

flow_velocity= float(input("Enter your flow velocity="))

flow_rate=calculate_flow_rate(pipe_area,flow_velocity)

print(f"Flow rate: {flow_rate} m^3/s")

def calculate_pipe_diameter(flow_rate, velocity):
    return math.sqrt(4 * (flow_rate/ (math.pi * velocity)))

required_flow_rate=0.10

flow_velocity=5

pipe_diameter = calculate_pipe_diameter(required_flow_rate, flow_velocity)

print(f"Required Pipe Diameter: {pipe_diameter} meters")

def calculate_pressure_drop(flow_rate, pipe_diameter, length, density, viscosity):
     
     friction_factor = 0.02
     
     return(friction_factor* length* density * (flow_rate ** 2)) / (2 * pipe_diameter)
 
pipe_length = 100
    
fluid_density = 1000
    
fluid_viscosity = .001
    
pressure_drop = calculate_pressure_drop(required_flow_rate, pipe_diameter, pipe_length, fluid_density, fluid_viscosity)

print(f"Pressure Drop: {pressure_drop} Pa")

user_flow_rate = float(input("Enter the desired flow rate (m^3)/s: "))

user_velocity = float(input("Enter the flow velocity (m/s):"))

user_pipe_diameter = calculate_pipe_diameter(user_flow_rate, user_velocity)

print(f"Required Pipe Diameter: {user_pipe_diameter} meters")


     