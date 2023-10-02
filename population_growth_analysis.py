import numpy as np
from prettytable import PrettyTable

# Define the parameters
initial_population_2004 = 20  # Initial population size in 2004 (per 10,000 m^2)
r_max_d = 1.15  # Maximum per capita growth rate under density-dependent conditions
K = 500  # Carrying capacity (maximum population size)
years = range(2004, 2015)  # Years from 2004 to 2014

# Initialize lists to store population sizes, r_max_d * N_t values, K-N_t/K values, ΔN/Δt values, and N_t+1 values over the years
population_sizes = []
r_max_d_values = []
k_minus_nt_over_k_values = []
delta_N_over_delta_t_values = []
next_population_values = []

# Calculate population size, r_max_d * N_t, K-N_t/K, ΔN/Δt, and N_t+1 for each year using the provided equation
current_population = initial_population_2004
for year in years:
    population_sizes.append(current_population)
    r_max_d_N_t = r_max_d * current_population
    r_max_d_values.append(r_max_d_N_t)
    k_minus_nt_over_k = (K - current_population) / K
    k_minus_nt_over_k_values.append(k_minus_nt_over_k)
    delta_N_over_delta_t = r_max_d_N_t * (1 - current_population / K)
    delta_N_over_delta_t_values.append(delta_N_over_delta_t)
    next_population = current_population + delta_N_over_delta_t
    next_population_values.append(next_population)
    current_population = next_population  # Update for the next iteration

# Create a PrettyTable
table = PrettyTable()
table.field_names = ["Year", "Population (per 10,000 m^2)", "r_max,d * N_t", "K-N_t/K", "ΔN/Δt", "N_t+1"]

# Populate the table with data
for year, population, r_max_d_N_t, k_minus_nt_k, delta_N_delta_t, next_pop in zip(
    years, population_sizes, r_max_d_values, k_minus_nt_over_k_values, delta_N_over_delta_t_values, next_population_values
):
    table.add_row([year, f"{population:.2f}", f"{r_max_d_N_t:.2f}", f"{k_minus_nt_k:.2f}", f"{delta_N_delta_t:.2f}", f"{next_pop:.2f}"])

# Display the table
print(table)
