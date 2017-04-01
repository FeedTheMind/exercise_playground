var Bob = function () { };

Bob.prototype.hey = function (input) {
  const i = input;

  if (!i.trim().length)
    return "Fine. Be that way!";

  if (i.toUpperCase() === i && /[A-Z]/.test(i))
    return "Whoa, chill out!";

  if (i.slice(-1) === '?')
    return "Sure.";

  return "Whatever.";

};

module.exports = Bob;
