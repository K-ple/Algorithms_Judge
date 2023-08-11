function solution(numbers) {
    let first = Math.max(...numbers)
    let check = []
    let double_check = []
    for (let i in numbers){
        if (numbers[i] !== first){
            check.push(numbers[i])
        }
        else{
            double_check.push(numbers[i])
        }
    }
    if(double_check.length >1){
        return first **2
    }
    return first * Math.max(...check)
}