public class SelectionSort {
    public static void print(int[] arr) {
        for(int ele: arr){
            System.out.print(ele+" ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int[] arr = {1,5,9,8,7,6,3,4,2};
        int n = arr.length;
        print(arr);

        for(int i=0; i<n; i++){
            int min = Integer.MAX_VALUE;
            int mindex = -1;
            for(int j=i; j<=n-1; j++){
                if(arr[j]<min){
                    min = arr[j];
                    mindex = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[mindex];
            arr[mindex] = temp;
        }
        print(arr);
    }
    
}


// stability of selection sort : selection sort is unstable bcz of ,agr repeated elements aate hain to after sorting
// vo us order me rehte hain jis order me vo sorting ke pehle the.(us order me reh bhi skte h or nhi bhi)