public class SEcondMax {
    public static void main(String[] args) { 
        int arr[] = {1,2,20,4,5,54,7,24,9};

        int max = Integer.MIN_VALUE;
        int smax = Integer.MIN_VALUE;

        for(int i=0; i<arr.length; i++){
            if(arr[i]>max) max=arr[i];
        }

        for(int i=0; i<arr.length; i++){
            if(arr[i]>smax && arr[i]!=max) smax=arr[i];
        }

        System.out.println("max elemenr is "+max);
        System.out.println("And second max element is "+smax);

    }
    
}
