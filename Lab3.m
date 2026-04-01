k = 2;
b = 1;
m = 2.5;
num = 1;
den = [m b k];
G = tf (num, den);

t = 0: 0.2:20;
step (G, t)

xlabel('Time')
ylabel('Amplitude')
title('Characteristics of second order system')
grid on;

clc;
clear;
close all;

% Original system
g = tf(0.4, [1 0.4 0.8]);

% Systems with additional poles
p1 = tf(1, [1 1]) * g; 
p2 = tf(1, [1 2]) * g;  
p3 = tf(1, [1 3]) * g;   

% Systems with additional zeros
z1 = tf([1 1], 1) * g;   % zero at -1
z2 = tf([1 0], 1) * g;   % zero at origin
z3 = tf([1 -1], 1) * g;  % zero at +1

% Time vector
t = 0:0.1:20;

%step responses
figure;
step(g, p1, p2, p3, z1, z2, z3, t);

% legend
legend('Original System', 'Pole at -1', 'Pole at -2', 'Pole at -3', ...
       'Zero at -1', 'Zero at 0', 'Zero at +1');

xlabel('Time (seconds)');
ylabel('Amplitude');
title('Effect of Poles and Zeros on System Response');
grid on;

clc;
clear;
close all;

% Original system 
g  = tf(0.4, [1 0.4 0.8]);

% Different damping conditions

% critically damped
d1 = tf(0.4, [1 1.78 0.8]);  
% overdamped
d2 = tf(0.4, [1 3.5777 0.8]);
% undamped
d3 = tf(0.4, [1 0 0.8]);       

% Time vector
t = 0:0.1:20;

% step responses
figure;
step(g, d1, d2, d3, t);

% legend
legend('Original System (Underdamped)', ...
       'Critically damped', ...
       'Overdamped', ...
       'Undamped');

xlabel('Time (seconds)');
ylabel('Amplitude');
title('Effect of Damping Ratio on System Response');
grid on;

k = 2;
b = 1;
m = 2.5;
num = 1;
den = [m b k];
G = tf (num, den);

t = 0: 0.2:20;
step (G, t)
xlabel('Time')
ylabel('Amplitude')
title('Characteristics of second order system')

poles = pole (G) ;
zeros = zero(G) ;

disp('Poles of transfer function:');
disp(poles) ;
disp('Zeros of transfer function: ');
disp(zeros) ;

pzmap (G);
grid on;