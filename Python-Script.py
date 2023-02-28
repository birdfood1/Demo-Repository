#%%
#========= Import Packages =======#

# OS = Operating System
import os
# Data Handling
import pandas as pd
# Plotting
import matplotlib.pyplot as plt

#======== Define Formatting =======#
# markers = ['v', 's', 'd', 'h', 'o']
#%%

#====== Select Directory =========#
hfr_dir = f'../Demo-Repository/HFR_Data/Experiment_1'
for i in os.listdir(hfr_dir):
    print(i)


for hfr_file in os.listdir(hfr_dir):

    #======== Load HFR Data ==========#
    temp_hfr_df = pd.read_csv(f'{hfr_dir}/{hfr_file}')

    #======= Define Variables ========#
    J = temp_hfr_df['Current Density (A/cm2)']
    V = temp_hfr_df['Potential (V)']
    HFR = temp_hfr_df['HFR (Ωcm2)']

    #====== Perform Calculation ======#
    V_HFR_free = V - J * HFR

    #====== Plot Calculation =========#
    plt.semilogx(J, V_HFR_free,'o', ls = 'none', mfc='none', label = hfr_file)
    plt.xlabel('HFR-free Voltage (V)')
    plt.ylabel('Current Density (A/cm$^2$)')
    plt.grid(alpha=0.35)
    plt.legend()

# %%
