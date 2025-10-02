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


class turboAs:
    """
    'n Klas wat 'n generiese turbo as modelleer.
    
    Eienskappe:
        traagheid (float): Die traagheid in [kg.m^2] van die 
                        turbine/kompressor as
    """
    
    def __init__(self, traagheid = 5):
        """
        Skep die geval van die turbo-as.
        
        Args:
            traagheid (float): Traagheid van turbine/kompressor as
                            in [kg.m^2].
        """
        self.traagheid = traagheid
        self.k = 1.4 # Lug konstante
        self.P1 = 0.1e6 # Druk in [Pa]
        self.P2 = self.P1*7
        self.P3 = self.P2
        self.P4 = self.P1
        self.T1 = 273.2 + 15 # Temperatuur in [K]
        self.T3 = 273.2 + 900
        self.Cp = 1004 # [J/kg.K]
        self.mdot = 8.1 # [kg/s] massavloei in enjin
        self.etac = 0.85 # Rendement van die kompressor
        self.etat = 0.9 # Rendement van die kompressor
        self.dP = 15000 # Drukval tussen die kompressor en turbine in [Pa]

        print(traagheid)
    
    def drywing(self):
        """
        Bereken die drywinguitset van die enjin.
        
        Returns:
            float: drywing van enjin in [kW].
        """

        self.T2s = self.T1*(self.P2/self.P1)**((self.k-1)/self.k)
        self.T2 = self.T1 + (self.T2s - self.T1)/self.etac
        self.wc = self.Cp*(self.T2 - self.T1) # [J/kg]
        self.Wc = self.wc*self.mdot # [W]

        self.P3 = self.P2 - self.dP # Drukval a.g.v. verliese
        self.T4s = self.T3*(self.P4/self.P3)**((self.k-1)/self.k)
        self.T4 = self.T3 - self.etat*(self.T3 - self.T4s)
        self.wt = self.Cp*(self.T3 - self.T4) # [J/kg]
        self.Wt = self.wt*self.mdot # [W]
        
        self.Wnet = self.Wt - self.Wc

        return self.Wnet
    
    def druk(self):
        print(f"T2s temperatuur {(self.T2s):.1f}K")
        print(f"Die kompressor werk is {self.Wc/1000:.1f}kW")
        print(f"Die turbine werk is {self.Wt/1000:.1f}kW")
        print(f"Die netto werk word bereken as {TV3117A.drywing()/1000:.1f}kW")

# %%
TV3117A = turboAs(0.3)
TV3117A.drywing()
#print(f"Die netto werk word bereken as {TV3117A.drywing()/1000:.1f}kW")
TV3117A.druk()

# %%
