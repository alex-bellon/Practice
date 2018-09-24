import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the candies function below.
    static long candies(int n, int[] arr) {
        long dist[] = new long[n];
        long result = 0;
        for (int i = 0; i < n; i ++){
            dist[i] = 1;
        }
        for (int i = 0; i < n; i ++){
            if(i - 1 >= 0 && arr[i - 1] > arr[i] && dist[i - 1] <= dist[i]) dist[i-1] = dist[i] + 1;
            if(i + 1 < n && arr[i + 1] > arr[i] && dist[i + 1] <= dist[i]) dist[i+1] = dist[i] + 1;
        }
        for (int i = 0; i < n; i ++){
            result += dist[i];
        }
        System.out.println(result);
        return result;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            int arrItem = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
            arr[i] = arrItem;
        }

        long result = candies(n, arr);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
