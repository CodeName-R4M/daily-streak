/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    let result = {};

    for (let i = 0; i < this.length; i++) {
        let key = fn(this[i]);

        if (!result[key]) {
            result[key] = [];
        }

        result[key].push(this[i]);
    }

    return result;
};