public class SecondOccurence {
    public static void main(String[] args) {
        int[] arr = {1,3,2,2,4,5,6,7,3,2,8,7,4};
        int idx = -1;
        int target = 4;

        int count = 0;

        for(int i=0; i<arr.length; i++){
            if(target==arr[i]){
                count++;
            }
            if(count==2){
            idx = i;
            break;
            }
        }
        if(idx!=-1) System.out.println("Second occurence of "+target+" at index "+idx);
        else System.out.println("element not found in array.");
    }
}
