
import java.util.Scanner;

public class magnitude {
   
   public static void main(String[] var0) {
      Scanner sc = new Scanner(System.in);
      System.out.println("Enetr a number:");
      int num = sc.nextInt();
      if (Math.abs(num) < 69) {
         System.out.println("the number is smaller than 69.");
      } else {
         System.out.println("the number is greater than 69.");
      }
   }
}

