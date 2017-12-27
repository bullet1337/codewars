// https://www.codewars.com/kata/559a28007caad2ac4e000083
import java.math.BigInteger;

public class SumFct {

    public static BigInteger perimeter(BigInteger n) {
        long nL = n.longValue();
        BigInteger sum = BigInteger.valueOf(2), a = BigInteger.ONE, b = BigInteger.ONE;

        while (nL-- >= 2) {
            BigInteger tmp = b;
            b = a.add(b);
            a = tmp;
            sum = sum.add(b);
        }

        return sum.multiply(BigInteger.valueOf(4L));
    }
}