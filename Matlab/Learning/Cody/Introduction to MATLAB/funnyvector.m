function vector = funnyvector(n)
    %Generate a vector like 1,2,2,3,3,3,4,4,4,4
    vector = [];
    for isize = 1:n
        for irepeat = 1:isize
            vector(end + 1) = isize;
        end
    end
end