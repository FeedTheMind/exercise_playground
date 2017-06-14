using System;

namespace ItsHipToBeSquare
{
    public static class Grains
    {
        public static ulong Square(int square) => 
            (ulong)Math.Pow(2, --square);

        public static ulong Total(int squares = 64)
        {
            ulong total = 0;

            for (int i = 1; i <= squares; i++) 
            {
                total += Square(i);
            }

            return total;
        }
    }
}
