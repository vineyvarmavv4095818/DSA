import java.util.Arrays;

public class ForEach {
    public static void main(String[] args) {
        int[] arr = {1,3,4,6,78,23,45,4,9};
        Arrays.sort(arr);
        for(int ele : arr){
            System.out.print(ele+" ");
        }
    }
    
}
