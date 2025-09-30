#%% Sonntag & Borgnakke, bl. 466.
import pyromat as pm
# %%
k = 1.4
P1 = 0.1e6
P2 = 1e6
P3 = P2
P4 = P1
T1 = 273.2 + 15
T3 = 273.2 + 1100
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
# %%
