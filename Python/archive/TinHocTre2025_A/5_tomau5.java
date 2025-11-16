import java.util.*;

public class 5_tomau5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();
        int N = sc.nextInt();

        long count = 0;

        for (int i = 0; i < M; i++) {
            long start = (long) N * i + 1;
            long end = start + N - 1;

            long start_multiple_5 = ((start + 4) / 5) * 5; // ceil to next multiple of 5
            long end_multiple_5 = (end / 5) * 5;           // floor to multiple of 5

            if (start <= start_multiple_5
                    && start_multiple_5 <= end
                    && start_multiple_5 > end_multiple_5) {
                System.out.println("Something is wrong? " + i + " " + start + " " + end
                        + " " + start_multiple_5 + " " + end_multiple_5);
            }

            if (start <= start_multiple_5 && start_multiple_5 <= end) {
                long numOfItem = (end_multiple_5 - start_multiple_5) / 5 + 1;

                long first = start_multiple_5 - start + 1;
                long last  = end_multiple_5 - start + 1;

                // sum of arithmetic series: numOfItem * (first + last) / 2
                long seriesSum = (first + last) * numOfItem / 2;

                count += seriesSum;
                count += (long) i * numOfItem;
                count %= 2025;
            }
        }

        System.out.println(count);
        sc.close();
    }
}
