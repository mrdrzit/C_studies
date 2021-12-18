function y = existsInVector(n, vector)
%Returns 1 if n exists in vector
    if sum(n==vector)
        y = 1;
    else
        y = 0;
    end
end