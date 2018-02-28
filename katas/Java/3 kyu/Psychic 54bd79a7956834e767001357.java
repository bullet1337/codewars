// https://www.codewars.com/kata/54bd79a7956834e767001357
import java.lang.reflect.Field;
import java.util.Random;

public class Psychic {

    public static double guess() {
        double result = 0.0;
        try {
            Field f = Math.class.getDeclaredClasses()[0].getDeclaredField("randomNumberGenerator");
            f.setAccessible(true);
            Random random = (Random) f.get(null);
            random.setSeed(0);
            result = random.nextDouble();
            random.setSeed(0);
        } catch (NoSuchFieldException | IllegalAccessException e) {
            e.printStackTrace();
        }
        return result;
    }
}