var createHelloWorld = function() {
    return function() {
        return("Hello World");
    }
};
  const f = createHelloWorld();
  const res=f();
  console.log(res);