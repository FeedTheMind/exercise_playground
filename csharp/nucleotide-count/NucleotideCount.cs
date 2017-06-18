using System;
using System.Collections.Generic;
using System.Linq;

namespace OneTwoNucleotidesComingForYou
{
    public class DNA
    {
        public readonly string SequenceDNA;
        public DNA(string sequence)
        {
            SequenceDNA = sequence;
        }

        public IDictionary<char, int> NucleotideCounts
        {
            get
            {
                IDictionary<char, int> dnaNucleotides= new Dictionary<char, int>
                {
                    {'A', 0},
                    {'T', 0},
                    {'C', 0},
                    {'G', 0}
                };

                foreach(char tide in SequenceDNA)
                {
                    dnaNucleotides[tide]++;
                }

                return dnaNucleotides;  
            }
        }

        public int Count(char nucleotide)
        {
            if (!NucleotideCounts.ContainsKey(nucleotide))
                throw new InvalidNucleotideException();

            return SequenceDNA.Count(x => x == nucleotide);
        }
    }

    public class InvalidNucleotideException : Exception { }
}
