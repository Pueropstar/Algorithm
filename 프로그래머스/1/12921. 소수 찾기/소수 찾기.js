function solution(n) {
    let arr = Array(n+1).fill(true).fill(false,0,2);
    
    for(let i = 2; i<Math.sqrt(n);i++){
        
        if(arr[i]){
            
            for(let j = i*i ; j<=n; j+=i){
                arr[j] = false;
            }
        }
    }
    return(arr.splice(2,n).filter(el=>el)).length
    
}