/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let finale=init
    if(nums.length != 0){
    for(i=0;i<nums.length;i++){
        finale=fn(finale,nums[i])
    }
    return finale
    }
    return init
};