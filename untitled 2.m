clc; clear;

f = @(x) 2*x.*cos(2*x) - (x + 1).^2;

a = -3; b = -2;

fprintf('Resultados de las iteraciones:\n');
for i = 1:3
    xi = b - (f(b)*(a - b)) / (f(a) - f(b));
    fprintf('Iteración %d: xi = %.4f, f(xi) = %.4f\n', i, xi, f(xi));
    
    if f(a) * f(xi) < 0
        b = xi;
    else
        a = xi;
    end
end


fplot(f, [a-1, b+1]);
hold on;
plot(xi, f(xi), 'ro');
grid on;
xlabel('x');
ylabel('f(x)');
title('Método de la Falsa Posición');

