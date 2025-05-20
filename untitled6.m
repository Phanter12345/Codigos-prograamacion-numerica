function y = f(x)
    y = 8 * x * sin(x) * exp(-x) - 1;
end

x0 = 0.5;       
x1 = -0.3;      
interacciones = 15;   

vx = [];  
for i = 1:interacciones
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0));  
    fprintf('Iteración %d: x = %.4f\n', i, x2);
    vx = [vx, x2];  
    x0 = x1;  
    x1 = x2;
end    


x = linspace(-1, 2, 100);
y = arrayfun(@f, x);
plot(x, y, 'b', 'LineWidth', 2);
hold on;
plot(vx, arrayfun(@f, vx), 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r');
grid on;
title('Método de la Secante');
xlabel('x');
ylabel('f(x)');
legend('f(x)', 'Aproximaciones de la raíz');
hold off;
