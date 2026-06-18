import java.util.Scanner;

public class array {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

            //  print sum of elements----->

        int[] arr = new int[5];
        System.out.print("Enetr elements:");
        for(int i=0; i<5; i++){
            arr[i] = sc.nextInt();
        }
        for(int i = 0; i<5; i++)

        if(arr[i]<0) System.out.println(arr[i]+" ");  //negative elements print krane ke liye.
        int sum = 0;
        for(int i=0; i<arr.length; i++){
            sum +=arr[i];
        }
        System.out.println(sum);

            //   print normal array----->

        // int[] arr = {12,-9,6,55,-44,8};
        // System.out.println(arr.length);
        // for(int i=0; i<arr.length; i++)
        //     System.out.print(arr[i]+" ");

            // zero array----->

        // int[] arr = new int[7];
        // for(int i = 0; i<7; i++)
        // System.out.print(arr[i]+" " );
    
    }
    
}
