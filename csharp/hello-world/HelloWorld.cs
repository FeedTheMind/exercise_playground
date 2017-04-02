public static class HelloWorld
{
    public static string Hello(string name)
    {
        if (name == null)
        {
            return "Hello, World!";
        }
        else
        {
            return $"Hello, {name}!";
        }
    }
}
