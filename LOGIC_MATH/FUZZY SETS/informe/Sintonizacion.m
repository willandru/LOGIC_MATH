clear all 
close all 

Tsim=590
Ts=0.3

X0=0.25
K=0.35
t0=8.5
Tau=13.5

%%%Empleando la Regla de Cohen Coon

mu=t0/Tau


Kc=(1/(mu*K))*(0.9+mu/12)
Ti=t0*((30+3*mu)/(9+20*mu))

out=sim('ModeloSK.slx')

