function old_name =  find_max_age(name, age)
    old_name = name(find(age == max(age)));
end