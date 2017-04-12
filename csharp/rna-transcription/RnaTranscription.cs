using System;
using System.Collections.Generic;

public static class Complement
{
    public static Dictionary<char, char> Dna2Rna = new Dictionary<char, char>()
    {
        {'C', 'G' },
        {'G', 'C' },
        {'T', 'A'},
        {'A', 'U'}
    };

    public static string OfDna(string dna)
    {
        string converted = "";
        foreach (char item in dna)
        {
            converted += Dna2Rna[item];
        }
        return converted;
    }
}
