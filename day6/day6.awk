
function frequency_counter(customs_form, num_people) {
    
    split(customs_form, answers, "")
    delete frequency
    for (i in answers) {
        frequency[answers[i]] = frequency[answers[i]] + 1
    }
    return length(frequency)
}


function group_answers(customs_form, num_people) {
    split(customs_form, answers, "")
    delete frequency
    for (j in answers) {
        if (answers[j] != ""){
            frequency[answers[j]] = frequency[answers[j]] + 1
        }
    }
    
    for(f in frequency){
        print f ":" frequency[f]
        if (frequency[f] != num_people) {
            return "false"
        }

    }
    return "true"
}

BEGIN {
    group[0]
    counter =0
}
NF > 0 {
        people = people + 1
        group[counter] = group[counter]$0
    }
NF == 0 {
    group[counter] = group[counter]" "frequency_counter(group[counter])
    group[counter] = group[counter]" "group_answers(group[counter], people)
    counter = counter +1
    people = 0
}
# make sure to check the last line
END {
    group[counter] = group[counter]" "frequency_counter(group[counter])
    group[counter] = group[counter]" "group_answers(group[counter], people)
    for (key in group) {
        print key , ":", group[key]
    } 
}

# awk -f day6.awk input.txt | awk '{sum = sum + $4} END {print sum}'