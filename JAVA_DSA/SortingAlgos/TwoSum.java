import java.util.Arrays;

public class TwoSum {
    public static void print(int[] arr, int target) {
        for(int ele: arr){
            System.out.print(ele+" ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int[] arr = {1,6,2,5,3,4,8,7};
        int n = arr.length;
        print(arr, 9);

        Arrays.sort(arr);
        int i = 0, j = n-1;

        while(i<j){
            if(arr[i]+arr[j]==9) {
                System.out.println(arr[i]+" "+arr[j]);
                i++;
                j--;
            }
            
            if(arr[i]+arr[j]>9) j--;
            if(arr[i]+arr[j]<9) i++;
            }
    }
    
}
