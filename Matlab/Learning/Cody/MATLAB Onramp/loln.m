function dice_diff = loln(N)
%If a large number of fair N-sided dice are rolled, the average of the simulated rolls is likely to be close to the mean of 1,2,...N i.e.
%the expected value of one die. For example, the expected value of a 6-sided die is 3.5.
%Given N, simulate 1e8 N-sided dice rolls by creating a vector of 1e8 uniformly distributed random integers. Return the difference
%between the mean of this vector and the mean of integers from 1 to N.
    rolls = randi(N,1,1e8);
    dice_diff = (sum(rolls)/length(rolls)) - sum((1:N))/N;
end