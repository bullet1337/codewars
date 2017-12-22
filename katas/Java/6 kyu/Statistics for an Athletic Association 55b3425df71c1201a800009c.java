// https://www.codewars.com/kata/55b3425df71c1201a800009c
import java.util.IntSummaryStatistics;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Stat {

    public static String stat(String strg) {
        List<Integer> results = Stream.of(strg.split(", ")).map(
                x -> Stream.of(x.split("\\|")).map(Integer::new).collect(Collectors.toList())
        ).map(x -> x.get(0) * 3600 + x.get(1) * 60 + x.get(2)).sorted().collect(Collectors.toList());

        IntSummaryStatistics stats = results.stream().mapToInt(x -> x).summaryStatistics();

        int range = stats.getMax() - stats.getMin(), avg = (int) stats.getAverage(),
                median = results.size() % 2 == 1
                                 ? results.get(results.size() / 2)
                                 : (results.get(results.size() / 2 - 1) + results.get(results.size() / 2)) / 2;

        return String.format("Range: %02d|%02d|%02d Average: %02d|%02d|%02d Median: %02d|%02d|%02d",
                             range / 3600, (range / 60) % 60, range % 60,
                             avg / 3600, (avg / 60) % 60, avg % 60,
                             median / 3600, (median / 60) % 60, median % 60);
    }
}
