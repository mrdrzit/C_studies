function b = isItSquared(a)
    for i = 1:length(a)
        if sum(a(i)*a(i) == a)
            b = true;
            break
        else
            b = false;
        end
    end
end