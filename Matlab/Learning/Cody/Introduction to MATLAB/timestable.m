function m = timestable(n)
%Write a function that outputs times tables up to the size requested
m = zeros(n,n);
    for i = 1:n
        m(i,:) = (1:n)*i;
    end
end

