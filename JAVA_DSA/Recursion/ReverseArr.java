public class ReverseArr {
    public static void reverseArr(int[] arr, int i, int j) {
        if(i>=j){
            return;
        }
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;

        reverseArr(arr, i+1, j-1);
    }
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5};
        for(int ele: arr){
            System.out.print(ele+" ");
        }
        System.out.println();
        int n = arr.length-1;
        reverseArr(arr, 0, n);
        for(int ele: arr){
            System.out.print(ele+" ");
        }
    }
}
