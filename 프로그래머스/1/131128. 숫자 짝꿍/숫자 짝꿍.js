function solution(X, Y) {
    var answer = '';
    let obj = {
        
    }
    for(const char of Y){
        obj[char] = (obj[char]||0) + 1;
    }
    console.log(obj)
    for(const char of X){
        if(obj[char] && obj[char] !== 0){
            obj[char]--;
            answer+=char;
        }
    }
    if (answer[0] == '0'){
        return "0";
    }
    if (answer.length === 0){   
        return "-1"
    }
    
    return [...answer].sort(function (a,b){
        if (a>b) return -1;
        if (a<b) return 1;
    }).join("");
}