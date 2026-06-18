public class OptimizeBubbleSort {
    public static void print(int[] arr) {
        for(int ele: arr){
            System.out.print(ele+" ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int[] arr = {1,-2,5,8,3,9,6,2};
        int n = arr.length;
        print(arr);
        for(int i = 0; i<n-1; i++){
            int swaps = 0; //boolean isSorted = true;
            for(int j = 0; j<n-1-i; j++){
                if(arr[j]>arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    swaps++; //isSorted = false;
                }
            }
            if(swaps==0) break; //if(isSorted==true) break;
        }
        print(arr);
    }
    
}
