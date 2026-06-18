public class SearchInArr {
    public static boolean exists(int[] arr, int target, int idx) {
        if(idx == arr.length) return false;
        if(arr[idx] == target) return true;
        return exists(arr, target, idx+1);
    }
    public static void main(String[] args) {
        int[] arr = {2,3,4,5,6,75,34,24};
        int target = 7;
        System.out.println(exists(arr, target,0));
    }
}