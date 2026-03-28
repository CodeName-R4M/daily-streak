/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {
    let filth = []
    let reali = []
    let i = 0
    for (i = 0; i < arr.length; i++) {
        filth[i] = fn(arr[i], i)
        if (filth[i] == true) {
            reali.push(arr[i])
        }
        else if (filth[i] == false) {
            continue
        }
        else if (typeof filth[i] === "number") {
            reali.push(arr[i])
        }
    }
    return reali
};