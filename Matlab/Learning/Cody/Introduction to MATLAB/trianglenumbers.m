function t = trianglenumbers(n)
    %Triangle numbers are the sums of successive integers. So 6 is a triangle number because 6 = 1 + 2 + 3
    % which can be displayed in a triangular shape like so
    %       *
    %      * *
    %     * * *
    % Thus 6 = triangle(3). Given n, return t, the triangular number for n.
    
    t=0;
    vector = 1:n;
    fprintf("The sequence is: %s\n", num2str(vector));
    for i = 1:n
        t = t+i;
    end
end