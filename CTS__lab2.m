clc;
clear all;
k=2;
b=3;
num=[1];
den=[b k];
G=tf(num,den)

t=0:0.2:20;
step(G,t)

xlabel('Time')
ylabel('Amplitude')
title('Characteristics of first order system')


