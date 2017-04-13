using System;
using System.Collections.Generic;
using System.Linq;

public static class SumOfMultiples
{
    public static int To(IEnumerable<int> multiples, int max)
    {
        IEnumerable<int> range = Enumerable.Range(0, max);
        
        return range.Where(n1 => multiples.Any(n2 => n1 % n2 == 0)).Sum();
    }
}
