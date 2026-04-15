/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let i=0
    let j=size
    let jung=arr.length/size
    let result=[]
    for(i=0;i<arr.length;i++){
        result.push(arr.slice(i,j))
        i=j-1
        j+=size
    }
    return result
};
