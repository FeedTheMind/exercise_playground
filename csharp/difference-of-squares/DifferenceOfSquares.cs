using System;

public static class Squares
{
    public static int SquareOfSums(int max)
    {
        int squareOfSums = 0;
        for(int i = 0; i <= max; i++)
        {
            squareOfSums += i;
        }
        return (int)Math.Pow(squareOfSums, 2);
    }

    public static int SumOfSquares(int max)
    {
        int sumOfSquares = 0;
        for (int i = 0; i <= max; i++)
        {
            sumOfSquares += (int)Math.Pow(i, 2);
        }
        return sumOfSquares;
    }

    public static int DifferenceOfSquares(int max)
    {
        return SquareOfSums(max) - SumOfSquares(max);
    }
}
