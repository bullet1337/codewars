// https://www.codewars.com/kata/5436f26c4e3d6c40e5000282
import static java.lang.Math.signum;

public class SequenceSum {
    public static int[] sumOfN(int n) {
        int sign = (int) signum(n);
        n *= sign;
        int[] result = new int[n + 1];
        result[0] = 0;

        for (int i = 1; i <= n; ++i) {
            result[i] = result[i - 1] + i * sign;
        }

        return result;
    }
}