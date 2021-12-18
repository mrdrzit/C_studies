%Find the maximum value in the given matrix.
% For example, if A = [1 2 3; 4 7 8; 0 9 1];
% then the answer is 9

function temp = matrixsz(x)
temp = 0;
for irow = 1:size(x,1)
    for icol = 1:size(x,2)
        if temp < x(irow,icol)
            temp = x(irow,icol);
        end
    end
end
end