// https://www.codewars.com/kata/54c27a33fb7da0db0100040e
import static java.lang.Math.floor;
import static java.lang.Math.sqrt;

public class Square {
    public static boolean isSquare(int n) {
        double sqrt = sqrt(n);
        return (sqrt - floor(sqrt)) < 1e-6;
    }
}