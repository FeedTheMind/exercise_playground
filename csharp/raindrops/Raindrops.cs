using System;

namespace TheSoundOfSilence
{
    public static class Raindrops
    {
        public static string Convert(int n)
        {
            string soundOrSilence = "";

            if (n % 3 == 0) 
                soundOrSilence += "Pling";

            if (n % 5 == 0) 
                soundOrSilence += "Plang";

            if (n % 7 == 0) 
                soundOrSilence += "Plong";

            return soundOrSilence == "" ? n.ToString() : soundOrSilence;
        }
    }
}
