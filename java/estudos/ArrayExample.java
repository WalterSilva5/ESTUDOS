import java.util.Arrays;

class ArrayExample{
  public static void main(String[] args){
    int[] nArray;

    nArray = new int[10];

    nArray[0] = 115;

    System.out.println("array is " + nArray);
    System.out.println("array str is: " + Arrays.toString(nArray));
  }
}