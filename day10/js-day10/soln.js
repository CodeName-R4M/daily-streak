/**
 * @param {Function} fn
 * @return {Function}
 */
 let firstc=new Set()
var once = function(fn) {
    
    return function(...args){
        if(firstc.has(fn)){
            return undefined
        }
        firstc.add(fn)
        return fn(...args)
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
