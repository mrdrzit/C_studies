function tf = mono_increase(vector)
    %Return true if the elements of the input vector increase monotonically 
    %(i.e. each element is larger than the previous).
    %Return false otherwise.

    for i = 1:length(vector)-1
        if vector(i+1) - vector(i) <= 0
            tf = false;
            break
        else
            tf = true;
        end
    end
end