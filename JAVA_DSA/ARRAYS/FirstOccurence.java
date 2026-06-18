public class FirstOccurence {
    public static void main(String[] args) {
        int[] arr = {1,4,8,2,4,5,7,2,9};
        int idx = -1;
        int target = 2;

        for(int i=0; i<arr.length; i++){
            if(target==arr[i]){
                idx = i;
                break;
            }
        }
        if(idx != -1) System.out.println("first occurence of "+target+" at index "+idx);
        else System.out.println("element not found in array.");
    }
}
