import java.util.Scanner;

public class FirstPattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for(int i=1; i<=5; i++){
            for(int j=1; j<=5+1-i; j++){
            // System.out.print((char)(j+64)+" ");

            // System.out.print((char)(i+64)+" ");

            // System.out.print("* ");

            // if(i%2==0) System.out.print((char)(j+64)+" ");
            // else System.out.print(j+" ");

            System.out.print("* ");


        }
        System.out.println();
        }
        
    }
    
    
}
