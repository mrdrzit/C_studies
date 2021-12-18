function [SA,SA2] = cake_frosting(r, h)
fprintf('Radius is %i\nHeight is %i',r,h)

%EDIT LATER

SA = 2*pi*r*(h + r);
SA2 = (2*pi*r*h)+(2*pi*r*r);

end