# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:27:37 2024

@author: User
"""
#structural_analysis_tool.py

import numpy as np

def calculate_reactions(load_positions, load_forces, span_length):
    total_load_moment = sum(load_positions * load_forces)
    
    reaction_A = total_load_moment / span_length
    
    reaction_B = sum(load_forces) - reaction_A
    
    return reaction_A, reaction_B

load_positions = np.array([2,5])

load_forces = np.array([10,20])

span_length = 6

reaction_A, reaction_B = calculate_reactions(load_positions, load_forces, span_length)

print(f"Reaction at A: {reaction_A} kN\nReaction at B: {reaction_B} kN")

def calculate_internal_forces(load_positions, load_forces, span_length, position):
    
    reaction_A = calculate_reactions(load_positions, load_forces, span_length)
    
    internal_moment = reaction_A * position - sum(load_forces[:np.argmax(load_positions >= position)] * (position - load_positions[:np.argmax(load_positions >= position)]))
    
    internal_shear = sum(load_forces[:np.argmax(load_positions >= position)])
    
    return internal_moment, internal_shear

position_of_interest = 4

moment, shear = calculate_internal_forces(load_positions, load_forces, span_length, position_of_interest)

print(f"Internal moment at {position_of_interest} meters: {moment} kNm\nInternal Shear at {position_of_interest} meters: {shear} kN")

user_load_positions = np.array(input("Enter corresponding load forces (comma-separated):").split(), dtype=float)

user_load_forces = np.array(input("Enter corresponding load forces (comma-separated):").split(), dtype=float)

user_span_length = float(input("Enter the span length:"))

input_string = ""

cleaned_string = input_string.replace("'","").replace(",","")

float_value = float(cleaned_string)

print(float_value)

user_reaction_A, user_reaction_B = calculate_reactions(user_load_positions, user_load_forces, user_span_length)

print(f"Reaction at A: {user_reaction_A} kN\nReaction at B: {user_reaction_B} kN")