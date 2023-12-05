import java.io.File;
import java.util.*;

public class DayThree {

    //this function finds the entire number given an x,y input for a matrix
    //returns a submatrix of that number window with its surrounding indexes, height is always 3
    static String[][] createSubMatrix(String[][] matrix, int[] x, int[] y, int[] num){
        int y1 = y[0]-1;
        int y2;
        int endX = x[0];
        int endY = y[0];
        int x1 = x[0] - 1;
        int x2 = x[0] + 1;
        if(x1 < 0){x1++;}
        if(x2 >= matrix.length){x2--;}

        //find the length of the number
        while(endY < matrix[0].length && Character.isDigit(matrix[endX][endY].toCharArray()[0])){
            //System.out.println(matrix[endX][endY]);
            num[0] = num[0]*10 + Integer.parseInt(matrix[endX][endY]);
            endY++;
        }
        y2 = endY;

        //System.out.println(num[0]);
        
        if(y2 > matrix[0].length){y2--;}

        if(y1 < 0){y1++;}

        y[0]=y2;

        String[][] subMatrix = new String[x2-x1+1][y2-y1+1];

        for(int i = 0; i < subMatrix.length && x1+i<matrix.length; i++){
            for(int j = 0; j < subMatrix[0].length  ; j++){
                //System.out.print("   "+(x1+i));
                //System.out.print("   "+(y1+j));
                subMatrix[i][j] = matrix[x1+i][y1+j];
            }
        }

        
        
        return subMatrix;
    }

    //method to return 0 if number has no surrounding symbols, and the number if it does
    static int validNumber(HashSet<String> symbols, String[][] matrix, int[] x,int[] y){
        //create pointer to store what number is found
        int[] num = {0};
        //create submatrix with given coordinates
        String[][] submatrix = createSubMatrix(matrix,x,y,num);
        //check if anything in the submatrix is a symbol, return 0 if no symbol found
        for(int i = 0; i < submatrix.length; i++){

            for(int j = 0; j < submatrix[0].length; j++){
                //return the number if the current character is not in our set of nums or '.'
                
                if(!symbols.contains(submatrix[i][j]) ){//&& submatrix[i][j] != null
                    for(String[] s:submatrix){
                        System.out.println(Arrays.toString(s));
                    }
                    System.out.println(num[0]);
                    System.out.println();
                    //System.out.println(submatrix[i][j]);
                    return num[0];
                }
            }

        }
        //return 0 if we only find nums or '.'
        return 0;
    }


    public static void main(String args[]){
        //Set of numbers and . to check for validity in submatrix
        HashSet<String> symbols = new HashSet<>();
        for(int i = 0; i <= 9; i++){
            symbols.add(""+i);
        }
        symbols.add(".");
        symbols.add("\r");

        //make the whole file a matrix of characters
        String content = "";
        try{
            content = new Scanner(new File("input3.txt")).useDelimiter("\\Z").next();
            
        } catch (Exception e){
            System.out.print(e);
        }

        String[] lines = content.split("\n");
        String[][] matrix = new String[lines.length][lines[0].length()];
        String[] currentLineSplit;

        //System.out.println(matrix.length);
        //System.out.println(matrix[139][0]);
        //System.out.println(matrix[0].length);
        

        for(int i = 0; i < matrix.length; i++){
            currentLineSplit = lines[i].split("");
            for(int j = 0; j < currentLineSplit.length; j++){
                matrix[i][j] = currentLineSplit[j];
            }
        }
        //System.out.println(matrix[139][0]);

        int sum = 0;
        
        //loop over every char, once a number is hit create a window for the whole number.
        for(int[] i = {0}; i[0] < matrix.length; i[0]++){
            //System.out.println(i[0]);
            for(int[] j = {0}; j[0] < matrix[0].length; j[0]++){
                //System.out.println(matrix[i[0]][j[0]]);
                //System.out.println(j[0]);
                //System.out.println(j[0]);
                if(matrix[i[0]][j[0]]!=null && Character.isDigit(matrix[i[0]][j[0]].toCharArray()[0])){
                    sum += validNumber(symbols,matrix,i,j);
                    //System.out.println(j[0]);
                }
                //System.out.println(sum);
            }
        }
        System.out.println(sum);
    }
}