#%% Modelleer 'n tipiese groot turbo as enjin
mdot = 8.1 # [kg/s]
# Air pressure ratio 7
# Gas generator 21200 rpm 
# Free turbine 12000 rpm
# Power nominal 1200hp, take-off 1500hp
# Turbine gas generator temperature 790 to 850 degC

# Starter torque 60N.m tot 5600opm
# Gas generator Rotor traagheid van 0.4 kg.m^2

# Stelsel traagheid 
#  Neem net die lemme vir eers (los uit die vry turbine, die ratkas, 
# stertrotor en ander ratkaste):
#  5 x 115kg met 'n swaartepunt van 3.3m van af die rotasie punt
# mr^2 = 115kg * 3.3^2  = 1252kg.m^2
# Met 5 lemme is dit 6261kg.m^2 traagheid.
# Aerodinamiese sleurkrag van 2.5kN.m per lem.  Tot maksimum van 240opm.

k = 1.4
P1 = 0.1e6
P2 = P1*7
P3 = P2
P4 = P1
T1 = 273.2 + 15
T3 = 273.2 + 900
Cp = 1004 # [J/kg.K]
mdot = 8.1 # [kg/s] massavloei in enjin
print(P2/P1)
# %%
T2 = T1*(P2/P1)**((k-1)/k)
wc = Cp*(T2 - T1) # [J/kg]
Wc = wc*mdot # [W]
print(f"Die kompressor werk is {Wc/1000:.1f}kW")
# %%
T4 = T3*(P4/P3)**((k-1)/k)
wt = Cp*(T3 - T4) # [J/kg]
Wt = wt*mdot # [W]
print(f"Die turbine werk is {Wt/1000:.1f}kW")
#%%
print(f"Die netto werk word bereken as {(Wt-Wc)/1000:.1f}kW")
print("Die maksimum uitset van die werklike turbine is 1640kW")
# %%
# Doen nou dieselfde berekening met doeltreffendheid van kompressor
# en turbine aannames.
# Dan 'n versnelling van die kompressor as en die las.

NR = 240*2*3.14159/60 # 240 opm
TR = 2.5*1000*5 # 2.5kN.m per rotor en 5 rotors
PR = TR*NR
print(f"Die drywing van hoofrotor is {(PR/1000):.1f}kW")
# %%
