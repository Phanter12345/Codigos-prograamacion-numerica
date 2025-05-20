function y = f(x)
    y = 2 * x * cos(2 * x) - (x + 1)^2;
end

a = -3;
b = -2;
iteraccion = 10;

for i = 1:iteraccion
    c = (a + b) / 2;
    if f(a) * f(c) < 0
        b = c;
    else
        a = c;
    end
    fprintf('Iteración %d: x = %.4f, intervalo = [%.4f, %.4f]\n', i, c, a, b);
end    


x = linspace(-3, -2, 100);
y = arrayfun(@f, x);
plot(x, y, 'b', 'LineWidth', 2);
hold on;
plot(c, f(c), 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r');
grid on;
title('Método de Bisección');
xlabel('x');
ylabel('f(x)');
legend('f(x)', 'Raíz estimada');
hold off;
