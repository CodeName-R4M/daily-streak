var compactObject = function(obj) {
    if (Array.isArray(obj)) {
        let res = [];
        for (let item of obj) {
            let compacted = compactObject(item);
            if (Boolean(compacted)) {
                res.push(compacted);
            }
        }
        return res;
    }

    if (obj !== null && typeof obj === "object") {
        let res = {};
        for (let key in obj) {
            let compacted = compactObject(obj[key]);
            if (Boolean(compacted)) {
                res[key] = compacted;
            }
        }
        return res;
    }

    return obj;
};