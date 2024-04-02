function solution(lottos, win_nums) {
    var answer = [];
    let arr = [];
    let min=0, max = 0;
    
    const award ={6:1,5:2,4:3,3:4,2:5,1:6,0:6};
    
    for(const num of lottos){
        if (win_nums.includes(num)){
            min++;
            max++;
        }
    }
    arr = lottos.filter((el)=> el == 0);
    max+=arr.length;
    answer.push(award[max])
    answer.push(award[min])
    return answer;
}