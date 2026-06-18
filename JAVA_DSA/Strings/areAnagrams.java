import java.util.Arrays;

public class areAnagrams {
    public static void main(String[] args) {
        String s1 = "tone";
        String s2 = "note";
        boolean isAnagram = true;
        if(s1.length()!=s2.length()) isAnagram = false;
        char[] arr1 = s1.toCharArray();
        char[] arr2 = s2.toCharArray();
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        for(int i=0; i<arr1.length; i++){
            if(arr1[i]!=arr2[i]) isAnagram = false;
        }
        System.out.println(isAnagram);
    }
}
