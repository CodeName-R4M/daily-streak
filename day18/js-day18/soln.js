/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */

    var timerr
var debounce = function(fn, t) {
    return function(...args) {
    clearTimeout(timerr)
    timerr=setTimeout(()=>{
        fn(...args)
    },t)
    }
    return clearTimeout(timerr)
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */