var HelloWorld = function() {};

HelloWorld.prototype.hello = function(input) {
    let name = input || 'World';

    return `Hello, ${name}!`
};

module.exports = HelloWorld;
