function Hamming() {}

Hamming.prototype.compute = function (one, two) {
  if (one.length !== two.length) {
    throw new Error('DNA strands must be of equal length.');
  }

  const split1 = one.split('');
  const split2 = two.split('');
  let diffHamm = 0;

  for (let i = 0; i < one.length; i++) {
    if (split1[i] !== split2[i]) {
      diffHamm++;
    }
  }

  return diffHamm;
};

module.exports = Hamming;
