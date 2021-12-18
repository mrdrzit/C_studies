function y = everyOther(vector)
    %Write a function which returns every other element of the vector passed in. 
    %That is, it returns the all odd-numbered elements, starting with the first.
    y = [];
    for i = 1:2:length(vector)
        y(end + 1) = vector(i);
    end
end