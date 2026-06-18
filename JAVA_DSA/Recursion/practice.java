import java.util.Scanner;

public class practice {
    public static void main(String[] args) {
        hanoi(4, 'A', 'B', 'C');
    }

    public static void hanoi(int n, char A, char B, char C) {
        if(n == 0) return;
        hanoi(n-1, A, C, B); //n-1 disks from A to C via B
        System.out.println(A+"->"+C); //largest disk from A to C
        hanoi(n-1, B, C, A); // n-1 disks from B to C via A
    }
}
