public class SecondOcc {
    public static int SecOcc(int[] arr, int target, int idx,int count){
        //base case
        if(idx==arr.length){
            return -1;
        }

        if(target==arr[idx]){
            count++;
        }
        if(count==2){
            return idx;
        }

        return SecOcc(arr, target, idx+1, count);
    }
    public static void main(String[] args) {
        int[] arr = {1,4,8,2,4,5,7,2,9};
        int target = 2;
        int result = SecOcc(arr, target, 0,0);

        if(result!=-1) System.out.println("first occurence of "+target+" at index "+result);
        else System.out.println("element not found in array.");
    }
}
