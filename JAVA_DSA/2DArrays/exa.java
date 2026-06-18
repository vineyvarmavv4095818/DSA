import java.util.Scanner;

public class exa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // int[][] arr = new int[3][4];
        int[][] arr = {{8,4,2,1},{2,9,6,3},{1,5,10,10}};
        System.out.println(arr.length+" "+arr[0].length);
        // for(int i=0; i<arr.length; i++){
        //     for(int j=0; j<arr[0].length; j++){
        //         arr[i][j] = sc.nextInt();
        //     }
        // System.out.println();
        // }
    //     for(int i=0; i<arr.length; i++){
    //         for(int j=0; j<arr[0].length; j++){
    //             System.out.print(arr[i][j]+" ");
    //         }
    //         System.out.println();
    // }
    int totalSum = 0;
    for(int i=0; i<arr.length; i++){
        for(int j = 0; j<arr[0].length; j++){
            totalSum += arr[i][j];
        }
    }
    System.out.println("sum: "+totalSum);

    int max = arr[0][0];
    for(int i=0; i<arr.length; i++){
        for(int j=0; j<arr[0].length; j++){
            if(arr[i][j]>max) max = arr[i][j];
        }
    }
    System.out.println("max element: "+max);

    int maxSum = Integer.MIN_VALUE;
    int row = -1;
    for(int i=0; i<arr.length; i++){
        int sum = 0;
        for(int j=0; j<arr[0].length; j++){
            sum += arr[i][j];
        }
    if(sum>maxSum){
    maxSum = Math.max(maxSum,sum);//maxSum = sum;(also can do this)
    row = i;
    }

    }
    System.out.println(row+" "+maxSum);
}
}
