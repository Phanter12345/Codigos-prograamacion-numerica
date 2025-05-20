clc; clear;

%  x^3 - 5x^2 + 5x - 1
p = [1 -5 5 -1];
x0 = 0.8;


for i = 1:3
    b = p(1);
    for j = 2:length(p)
        b(j) = p(j) + x0 * b(j-1);
    end
    x0 = x0 - b(end) / b(end-1);
end


A = b(1); B = b(2); C = b(3);
x1 = (-B + sqrt(B^2 - 4*A*C)) / (2*A);
x2 = (-B - sqrt(B^2 - 4*A*C)) / (2*A);

fprintf('Raíces: %.4f, %.4f, %.4f\n', x0, x1, x2);


fplot(@(x) polyval(p, x), [-1, 3]); hold on;
plot([x0, x1, x2], [0, 0, 0], 'ro');