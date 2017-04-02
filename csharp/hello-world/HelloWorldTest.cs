using Xunit;

public class HelloWorldTest
{
    [Fact]
    public void Say_hi()
    {
        Assert.Equal("Hello, World!", HelloWorld.Hello(null));
    }

    [Fact]
    public void some_name()
    {
        Assert.Equal("Hello, Dude(tte)!", HelloWorld.Hello("Dude(tte)"));
    }
}
