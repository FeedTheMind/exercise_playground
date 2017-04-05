using System;

public static class Gigasecond
{
    public static DateTime Date(DateTime birthDate)
    {
        double gigasecond = Math.Pow(10, 9);
        return birthDate.AddSeconds(gigasecond);
    }
}
