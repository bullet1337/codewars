// https://www.codewars.com/kata/550f22f4d758534c1100025a
import java.util.*;

public class DirReduction {
    static Map<String, String> reverseMap = new HashMap<>();

    static {
        reverseMap.put("NORTH", "SOUTH");
        reverseMap.put("SOUTH", "NORTH");
        reverseMap.put("EAST", "WEST");
        reverseMap.put("WEST", "EAST");
    }

    public static String[] dirReduc(String[] arr) {
        LinkedList<String> path = new LinkedList<>();
        for (String direction : arr) {
            if (path.size() == 0) {
                path.add(direction);
            } else {
                if (direction.equals(path.peekLast())) {
                    path.add(direction);
                } else {
                    if (!reverseMap.get(direction).equals(path.peekLast())) {
                        path.add(direction);
                    } else {
                        path.removeLast();
                    }
                }
            }
        }

        return path.toArray(new String[path.size()]);
    }
}
