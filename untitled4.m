function y = f(x)
    y = 8 * x * sin(x) * exp(-x) - 1;
end

function dy = df(x)
    dy = 8 * sin(x) * exp(-x) + 8 * x * cos(x) * exp(-x) - 8 * x * sin(x) * exp(-x);
end

x0 = 0.3;      
iteraccion = 10;    

vx = [];  

for i = 1:iteraccion
    x1 = x0 - f(x0) / df(x0);  
    fprintf('Iteración %d: x = %.4f\n', i, x1);
    vx = [vx, x1];  
    x0 = x1;  
end    


x = linspace(-1, 2, 100);
y = arrayfun(@f, x);
plot(x, y, 'b', 'LineWidth', 2);
hold on;
plot(valores_x, arrayfun(@f, valores_x), 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r');
grid on;
title('Método de Newton-Raphson');
xlabel('x');
ylabel('f(x)');
legend('f(x)', 'Aproximaciones de la raíz');
hold off;
