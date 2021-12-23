function vector = funnyvector(n)
    %Generate a vector like 1,2,2,3,3,3,4,4,4,4
    vector = zeros(sum(1:n),1);
    i=1;
    for isize = 1:n
        for irepeat = 1:isize
            vector(i) = isize;
            i=i+1;
        end
    end
end