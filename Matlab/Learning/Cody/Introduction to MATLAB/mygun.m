function mygun(Presence, Number)

    if Presence == 1
        spitTheTruth(Number)
    else
        fprintf('You can''t handle the truth\n');
    end

end
   

function spitTheTruth(Number)
    for i=1:Number
        fprintf('42\n')
    end
end

%This is a comment