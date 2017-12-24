// https://www.codewars.com/kata/5259510fc76e59579e0009d4
public class Dictionary {
    private final String[] words;

    public Dictionary(String[] words) {
        this.words = words;
    }

    int editdist(String S1, String S2) {
        int m = S1.length(), n = S2.length();
        int[] D1, D2 = new int[n + 1];

        for (int i = 0; i <= n; ++i) {
            D2[i] = i;
        }

        for (int i = 1; i <= m; ++i) {
            D1 = D2;
            D2 = new int[n + 1];

            for (int j = 0; j <= n; ++j) {
                if (j == 0) {
                    D2[j] = i;
                } else {
                    int cost = (S1.charAt(i - 1) != S2.charAt(j - 1)) ? 1 : 0;
                    if (D2[j - 1] < D1[j] && D2[j - 1] < D1[j - 1] + cost) {
                        D2[j] = D2[j - 1] + 1;
                    } else if (D1[j] < D1[j - 1] + cost) {
                        D2[j] = D1[j] + 1;
                    } else {
                        D2[j] = D1[j - 1] + cost;
                    }
                }
            }
        }
        
        return D2[n];
    }

    public String findMostSimilar(String to) {
        int minDist = Integer.MAX_VALUE;
        String word = null;
        for (String w : words) {
            int dist = editdist(to, w);
            if (dist < minDist) {
                minDist = dist;
                word = w;
            }
        }

        return word;
    }
}