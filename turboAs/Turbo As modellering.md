Modelleer 'n turbo-as enjin in python.  Die doel is om dit later te vertaal in C++ sodat dit vir helikopter modellering in JSBsim gebruik kan word.

Hier volg die prosesvloei diagram wat gebruik word:

![[TurboAs Diagram|500]]

Die veranderlikes van die simulasie is die traagheid van die kompressor/turbine as en die traagheid van die vry turbine.  Die versnelling van die kompressor turbine as is as volg:

$$
\alpha_{kt} = \frac{T_{kt} - T_{kta}}{I_{kt}}
$$
Die draaimoment van die kompressor/turbine as kompressor is die som van die knormoer draaimoment en die draaimoment van die turbine.

$$
T_{kt} = T_k + T_{turb}
$$
Die versnelling van die vry turbine is 'n funksie van die traagheid van die stelsel wat dit aandryf en die aërodinamiese weerstand van die stelsel:
$$
\alpha_{t} = \frac{T_t - T_s}{I_{s}}
$$

### Nomenklatuur


| Simbool       | Beskrywing                                         |
| ------------- | -------------------------------------------------- |
| $\alpha_{kt}$ | Versnelling van die kompressor/turbine as          |
| $T_{kt}$      | Draaimoment van die kompressor/turbine as          |
| $I_{kt}$      | Traagheid van die kompressor/turbine as            |
| $T_k$         | Draaimoment van die knormoer                       |
| $T_{turb}$    | Draaimoment van die turbine                        |
| $T_t$         | Draaimoment van die vry turbine                    |
| $I_s$         | Traagheid van die stelsel wat aangedryf word       |
| $T_s$         | Aërodinamiese weerstand van die stelsel            |
| $T_{kta}$     | Aërodinamiese weerstand van die kompressor/turbine |
