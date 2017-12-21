// https://www.codewars.com/kata/534ea96ebb17181947000ada
public class Chocolate{

    public static int breakChocolate(int n, int m) {
        return n == 0 || m == 0 || n == 1 && m == 1 ? 0 : n * m - 1;
    }
}