function solution(num_list) {
    let j = 0
    let h = 0
    for(let i in num_list){
        if (num_list[i] % 2 === 0){
            j+= 1;
        }
    else{
        h += 1;
    }
    }
    return [j,h];
}