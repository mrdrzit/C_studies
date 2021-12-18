function y = reverseVector(vector)
    %Reverse a vector of n elements
    start_pointer = 1;
    end_pointer = length(vector);

    for i = 1:floor(length(vector)/2.0)
        swap_temp = vector(i);
        vector(i) = vector(end_pointer);
        vector(end_pointer) = swap_temp;
        end_pointer = end_pointer - 1;
        start_pointer = start_pointer + 1;
    end
    y = vector;
end