function solution(X, Y) {
    var answer = '';
    let copy = JSON.parse(JSON.stringify(Y));
    let target_obj = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0};
    
    for (let i = 0 ;i<Y.length;i++){
        target_obj[Y[i]]++;
    }
    for(let i = 0 ;i<X.length; i++){
        if(target_obj[X[i]] !==0){
            target_obj[X[i]]--;
            answer+=X[i];
        }
    }
    const answer_arr = Array.from(answer);
    if (answer[0] == '0'){
        return "0";
    }
    else if (answer.length == 0){   
        return "-1"
    }
    
    return answer_arr.sort(function (a,b){
        if (a>b) return -1;
        if (a<b) return 1;
    }).join("");
}