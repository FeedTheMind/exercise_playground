using System;

public class SpaceAge
{
  private long ageInSeconds;
  public const double EARTH_SECONDS_In_Year = 31557600;

    public SpaceAge(long seconds)
    {
        this.ageInSeconds = seconds;
    }

    public double OnEarth()
    {
    return AgeOfPerson(1);
    }

    public double OnMercury()
    {
        return AgeOfPerson(0.2408467);
    }

    public double OnVenus()
    {
        return AgeOfPerson(0.61519726);
    }

    public double OnMars()
    {
        return AgeOfPerson(1.8808158);
    }

    public double OnJupiter()
    {
        return AgeOfPerson(11.862615);
    }

    public double OnSaturn()
    {
        return AgeOfPerson(29.447498);
    }

    public double OnUranus()
    {
        return AgeOfPerson(84.016846);
    }

    public double OnNeptune()
    {
        return AgeOfPerson(164.79132);
    }

    public double AgeOfPerson(double orbitalPeriod)
    {
        return Math.Round(ageInSeconds / (EARTH_SECONDS_In_Year * orbitalPeriod), 2);
    }
}
