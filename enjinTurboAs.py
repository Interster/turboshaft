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