import java.util.Scanner;

public class If_Else {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter a number:");
        int num = sc.nextInt();

        int magnitude = Math.abs(num);

        if(magnitude > 69) System.out.println("the number is greater than 69.");
        else if(magnitude == 69) System.out.println("the number is equal to 69");
        else System.out.println("the number is smaller than 69");
    }
}