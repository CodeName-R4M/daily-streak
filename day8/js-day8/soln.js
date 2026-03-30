/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    
    return function(x) {
        let lasst=x
    for(i=functions.length-1;i>=0;i--){
        if(i==functions){
        lasst=functions[i](x)
        }
        else{
            lasst=functions[i](lasst)
        }
    }
    return lasst
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */