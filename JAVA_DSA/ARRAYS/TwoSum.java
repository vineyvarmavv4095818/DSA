import java.util.Scanner;

public class TwoSum {
    public static void main(String[] args) {
        int arr[] = {1,2,3,4,5};
        int target = 6;
        twosum(arr, target);

        
    }
    public static void twosum(int arr[], int target) {
        
        int n = arr.length;
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                if(arr[i]+arr[j] == target)
                    System.out.println("["+arr[i]+","+arr[j]+"]");
                    


            }
        }
        
    }
}
