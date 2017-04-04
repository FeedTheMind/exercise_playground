public static class Bob
{
    public static string Hey(string statement)
    {
        string sentence = statement.Trim();
        string yell = sentence.ToUpper();
        string normal = sentence.ToLower();

        if (sentence == "")
        {
            return "Fine. Be that way!";
        }
        if (sentence == yell && sentence != normal)
        {
            return "Whoa, chill out!";
        }
        if (sentence.Substring(sentence.Length-1, 1) == "?")
        {
            return "Sure.";
        }

        return "Whatever.";
    }
}
