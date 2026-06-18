public class kthSmallest {
    public static int print(int[] arr, int k) {
        int n = arr.length;
        

        for(int i=0; i<k; i++){
            int min = Integer.MAX_VALUE;
            int mindex = -1;
            for(int j=i; j<n; j++){
                if(arr[j]<min){
                    min = arr[j];
                    mindex = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[mindex];
            arr[mindex] = temp;
        }
        return arr[k-1];
    }
    public static void main(String[] args) {
        int[] arr = {9,8,7,6,5};
        int k = 3;

        int result = print(arr, k);
        System.out.println(result);

        
    }

}
