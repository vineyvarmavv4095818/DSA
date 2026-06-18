import java.util.Arrays;

public class SortArray {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,33,21,54,-5,5};

        // 1.original array
        print(arr);

        // 2.sort array
        Arrays.sort(arr);
        print(arr);

        // 3.modify array
        for(int i = 0; i<arr.length; i++){
            if(i%2==0) arr[i]+=10;
        else arr[i]*=2;
        }
        // 4.print modified array
        print(arr);
        

        
    }
    public static void print(int[] arr) {
        for(int i = 0; i<arr.length; i++) {
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }

}
