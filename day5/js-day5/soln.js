/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    newman=[]
    for(i=0;i<arr.length;i++){
        newman[i]=fn(arr[i],i)
    }
    return newman
};