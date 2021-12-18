function out = findIndices(vec, thresh)
    %Given a vector, vec, return the indices where vec is greater than scalar, thresh.
    out = find((thresh<vec));
end