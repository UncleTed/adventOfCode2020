
function frequency_counter(customs_form) {
    
    split(customs_form, answers, "")
    delete frequency
    for (i in answers) {
        frequency[answers[i]] = 1
    }
    return length(frequency)
}

BEGIN {
    group[0]
    counter =0
}
NF > 0 {
        group[counter] = group[counter]$0
    }
NF == 0 {
    group[counter] = group[counter]" "frequency_counter(group[counter])
    counter = counter +1
   
}
# make sure to check the last line
END {
    group[counter] = group[counter]" "frequency_counter(group[counter])
    for (key in group) {
        print key , ":", group[key]
    } 
}