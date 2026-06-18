public class pushZerosToEnd {
    public static void print(int[] arr) {
        for(int ele: arr){
            System.out.print(ele+" ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int[] arr = {2,-9,4,1,5,0,3,0,-4,2,0};
        int n = arr.length;
        print(arr);

        for(int i=0; i<n-1; i++){
            boolean isOk = true;
            for(int j=0; j<n-1-i; j++){
                if(arr[j]==0){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    isOk = false;
                }
            }
            if(isOk==true) break;
        }
        print(arr);
    }

}
