// https://www.codewars.com/kata/582c1092306063791c000c00
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import static java.lang.Math.min;
import static java.lang.Math.pow;

public class InfiniteDigitalString {

    public static long split(String s, int partSize) {
        int tailPartSize;
        long last, current, first;
        String head, tail;
        List<Long> results = new ArrayList<>();
        for (int i = 0; i < partSize; ++i) {
            tailPartSize = partSize;
            tail = "";
            head = "";
            last = first = -1;
            boolean add = true;
            int j = i;
            for (; j + tailPartSize <= s.length(); j += tailPartSize) {
                if (s.charAt(j) == '0') {
                    add = false;
                    break;
                }

                current = Long.valueOf(s.substring(j, j + tailPartSize));
                if (last == -1) {
                    first = current;
                    last = current;
                } else {
                    if (last != current - 1) {
                        if (last == (long) pow(10, tailPartSize) - 1) {
                            String moreDigits = s.substring(j, min(j + ++tailPartSize, s.length()));
                            if (moreDigits.matches("\\d0{0," + tailPartSize + "}")) {
                                if (moreDigits.charAt(0) != '1' && head.equals("")) {
                                    head = String.valueOf(first);
                                    first = Long.valueOf(moreDigits)
                                                    * (long) pow(10, tailPartSize - moreDigits.length());
                                } else {
                                    if (moreDigits.length() < tailPartSize) {
                                        tail = moreDigits;
                                    } else {
                                        current = Long.valueOf(moreDigits);
                                    }
                                }
                            } else {
                                add = false;
                                break;
                            }
                        } else {
                            add = false;
                            break;
                        }
                    }
                    last = current;
                }
            }

            if (add) {
                if (head.equals("") && i > 0) {
                    head = s.substring(0, i);
                    if (!(first == -1 || String.valueOf(first - 1).endsWith(head))) {
                        continue;
                    }
                }

                if (tail.equals("") && j < s.length()) {
                    if (s.charAt(j) == '0') {
                        continue;
                    }

                    tail = s.substring(j, s.length());
                    if (!(last == -1 || String.valueOf(last + 1).startsWith(tail))) {
                        continue;
                    }
                }

                if (first != -1) {
                    results.add(calcOffset(first) - head.length());
                } else {
                    long res = resolve(head, tail, partSize);
                    if (res != -1) {
                        results.add(calcOffset(res) + partSize - head.length());
                    }
                }
            }
        }

        return results.stream().mapToLong(x -> x).min().orElse(-1);
    }

    private static long resolve(String head, String tail, int headPartSize) {
        if (headPartSize == head.length() + tail.length()) {
            return Long.valueOf(tail + head);
        }

        String newHead = String.valueOf(Long.valueOf(head) + 1);
        newHead = String.join("", Collections.nCopies(head.length() - newHead.length(), "0")) + newHead;
        if (tail.endsWith(newHead.substring(0, tail.length() - (headPartSize - head.length())))) {
            return Long.valueOf(tail.substring(0, headPartSize - head.length()) + head);
        }

        return -1;
    }

    public static long calcOffset(long number) {
        String str = String.valueOf(number);
        int digits = str.length();

        long offset = 0;
        for (int i = 1; i < digits; ++i) {
            offset += i * (9 * (long) pow(10, i - 1));
        }

        return offset + digits * (number - (long) pow(10, digits - 1));
    }

    public static long findPosition(String s) {
        if (s.matches("0+")) {
            return calcOffset(Long.valueOf("1" + s)) + 1;
        }

        long x = -1;
        for (int i = 1; i <= s.length(); ++i) {
            x = split(s, i);
            if (x != -1) {
                break;
            }
        }

        return x == -1 ? calcOffset(Long.valueOf(s)) : x;
    }
}