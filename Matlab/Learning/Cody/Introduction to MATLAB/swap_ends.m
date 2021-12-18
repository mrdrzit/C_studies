function B = swap_ends(A)
%Flip the outermost columns of matrix A, so that the first column becomes the last and the last column becomes the first.
%All other columns should be left intact. Return the result in matrix B.

    tmp = A(:,1);
    A(:,1) = A(:,end);
    A(:,end) = tmp;
    B = A;
end