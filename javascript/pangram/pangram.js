let Pangram = function (sentence) {
	this.alphabet = [...'abcdefghijklmnopqrstuvwxyz'];
	this.sentence = sentence;
};

Pangram.prototype.isPangram = function () {
	const filtered = this.sentence.split('').filter(letter => {
		return (letter.match(/[a-z, A-Z]/)); 
	}).join('').toLowerCase();

	for (let i = 0; i < this.alphabet.length; i++) {
		if (filtered.indexOf(this.alphabet[i]) < 0) {
			return false;
		}
	}
	
	return true;
};

module.exports = Pangram;
