public class InsertionSort {
    public static void main(String[] args) {
        int[] arr = {2,7,4,3,9,6,5,8,1};
        int n = arr.length;
        for(int i = 1; i<n; i++){
        int j = i;
        while(j>0 && arr[j]<arr[j-1]){ //insertion sort me do array ko compare krte hain mtlb ek hi array ke do parts ko. yaha pehla part 2 hoga dusre part me sbhi elements honge
            int temp = arr[j];
            arr[j] = arr[j-1];
            arr[j-1] = temp;
            j--;
            }
        }
        for(int ele: arr){
            System.out.print(ele+" ");
        }
    }
    
}
