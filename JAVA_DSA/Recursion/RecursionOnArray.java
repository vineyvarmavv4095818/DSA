public class RecursionOnArray {
    public static void main(String[] args) {
        int[] arr = {23,4,32,1,56,7,98,45,2};
        recPrint(arr, 0);
    }
    public static void recPrint(int[] arr, int idx) {
        if(idx==arr.length-1){
            System.out.print(arr[idx]+" ");
            return;
        }
        // if(idx==arr.length) return;  agr first element ko do bar print krna hai to ye likho
        System.out.print(arr[idx]+" ");
        recPrint(arr, idx+1);
        System.out.print(arr[idx]+" ");
    }
}
