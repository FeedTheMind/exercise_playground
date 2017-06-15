using System;
using System.Linq;

namespace HisNameWasRobertPaulson
{
    public static class Pangram
    {
        public const string ABCs = "abcdefghijklmnopqrstuvwxyz";
        
        public static bool IsPangram(string sentence)
        {
            return ABCs.All(letter => sentence.ToLower().Contains(letter));
        }
    }
}
