let cache = new Map()
var TimeLimitedCache = function () {

};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function (key, value, duration) {
    if (cache.has(key)) {
        let item = cache.get(key)
        if (Date.now() > item.expiry) {
            cache.delete(key);
            cache.set(key, { value: value, expiry: Date.now() + duration })
            return false;
        }
        cache.set(key, { value: value, expiry: Date.now() + duration })
        return true
    }
    cache.set(key, { value, expiry: Date.now() + duration })
    return false
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function (key) {
    if (cache.has(key)) {
        if (Date.now() > cache.get(key).expiry) {
            cache.delete(key)
            return -1
        } else {
            return cache.get(key).value
        }
    } else {
        return -1
    }
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function () {
    let countr = 0;
    const now = Date.now();
    for (const [key, item] of cache) {
        if (item.expiry > now) {
            countr++;
        }
    }

    return countr;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */