using System;
using System.Linq;

namespace NucleoTidesOfMan
{
    public static class Hamming
    {
        public static int Compute(string strand1, string strand2)
        {
            return strand1.Zip(strand2, (one, two) =>
                one.Equals(two) ? 0 : 1).Sum();
        }
    }
}
