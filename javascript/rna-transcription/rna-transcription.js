var DnaTranscriber = function () {
  this.dnaMap = {G: 'C', C: 'G', T: 'A', A: 'U'};
};

DnaTranscriber.prototype.toRna = function (DNA) {
  const dna2RNA = this.dnaMap;
  const upperSplit = DNA.toUpperCase().split('');

  return upperSplit.map(i => {
    if (i in dna2RNA) {
      return dna2RNA[i];
    } else {
      throw new Error('Invalid input');
    }
  }).join('');  
};

module.exports = DnaTranscriber;
