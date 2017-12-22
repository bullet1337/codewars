// https://www.codewars.com/kata/52742f58faf5485cae000b9a
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class TimeFormatter {

    public static String formatDuration(int seconds) {
        if (seconds == 0) {
            return "now";
        }

        int secondsInHour = 60 * 60, secondsInDay = 24 * secondsInHour, secondsInYear = 365 * secondsInDay;
        Map<String, Integer> dateMap = new LinkedHashMap<>();
        dateMap.put("year", seconds / secondsInYear);
        dateMap.put("day", (seconds % secondsInYear) / secondsInDay);
        dateMap.put("hour", (seconds % secondsInDay) / secondsInHour);
        dateMap.put("minute", (seconds % secondsInHour) / 60);
        dateMap.put("second", seconds % 60);
        dateMap.entrySet().removeIf(e -> e.getValue() == 0);

        List<String> results
                = dateMap.entrySet().stream()
                         .map(e -> String.format("%d %s%s", e.getValue(), e.getKey(), e.getValue() == 1 ? "" : "s"))
                         .collect(Collectors.toList());

        return String.join(", ", results.subList(0, results.size() - 1)) + (results.size() > 1 ?  " and " : "")
                + results.get(results.size() - 1);
    }
}