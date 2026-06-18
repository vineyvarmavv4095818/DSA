
public class BubbleSort {
    public static void print(int[] arr){
        for(int ele: arr){
            System.out.print(ele+" ");
        }
        System.out.println();
    }
public static void main(String[] args) {
    int[] arr = {-1,3,5,7,6,0,1,3,4,-3,-2};
    int n = arr.length;
    print(arr);
        
    for(int i = 0; i<n-1; i++){
        boolean isSorted = true;
        for(int k =0; k<n-1; k++){
            if(arr[k]>arr[k+1]){
                isSorted = false;
                break;  //kyuki ek bar me hi unsorted pair mil jayega to jo ye k wala loop h aage chlane ki jrrt nhi h
            }
        }
        if(isSorted==true) break; // agr issorted true hi rha to main for loop ko aage chlane ki jrurt nhi hai.
        for(int j = 0; j<n-i-1; j++){
            if(arr[j]>arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;

            }
        }
    }
        print(arr);
    }
}


// stability of bubble sort : bubble sort is stable bcz of ,agr repeated elements aate hain to after sorting 
// vo usi order me rehte hain jis order me vo sorting ke pehle the