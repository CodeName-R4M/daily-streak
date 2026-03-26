var createCounter = function(init) {
    let val=init
    return {
        increment(){return ++init},decrement(){return --init},reset(){init=val;return init}}
};