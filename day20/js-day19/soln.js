/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    if(obj==null){
        return false
    }
    if(Array.isArray(obj)){
        if(obj.length>=1){
            return false
        }
    }
    if(Object.keys(obj).length>=1){
        return false
    }
    return true
};