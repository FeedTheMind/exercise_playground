function Hamming() {}

Hamming.prototype.compute = function (one, two) {
  let strand1 = one.length;
  let strand2 = two.length;

  if (strand1 !== strand2) {
    throw new Error('DNA strands must be of equal length.')
  }
}

module.exports = Hamming;
