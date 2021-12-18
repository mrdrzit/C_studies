function y = column_removal(matrix, column)
    %Remove the nth column from input matrix A and return the resulting matrix in output B.
    y = [];
    for i = 1:size(matrix, 2)
        if i == column
            continue
        else
            tmp = matrix(:,i);
            y = [y,tmp];
        end
    end
end