import java.util.Scanner;

public class SeriesPrinting {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("ENter a number:");
        int num = sc.nextInt();

        int count = 0;
        while (num!=0) {
        num/=10;
            count++;
        }
        System.out.println(count);


        // for (int i = 99; i > 0; i -= 4){
        // //     System.out.print(i+" ");

    // int sum = 0;
    // while(num!=0){
    //     sum+=(num%10);
    //     num = num/10;
    
    // }
    // System.out.println(sum);
    


}
    
}
