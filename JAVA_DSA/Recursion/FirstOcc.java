public class FirstOcc {
    public static int FirOcc(int[] arr, int target, int idx){
        //base case
        if(idx==arr.length){
            return -1;
        }

        if(target==arr[idx]){
            return idx;
        }

        return FirOcc(arr, target, idx+1);
    }
    public static void main(String[] args) {
        int[] arr = {1,4,8,2,4,5,7,2,9};
        int target = 2;
        int result = FirOcc(arr, target, 0);

        if(result!=-1) System.out.println("first occurence of "+target+" at index "+result);
        else System.out.println("element not found in array.");
    }
}
