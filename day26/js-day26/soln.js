/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    let res=[]
    for(let i=0;i<arr.length;i++){
        if(Array.isArray(arr[i]) && n>0){
        let temp = flat(arr[i], n - 1);
        for (let j = 0; j < temp.length; j++) {
            res.push(temp[j]);
        }
    }
    else{
        res.push(arr[i])
    }
    }
    return res
};