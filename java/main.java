
import java.io.*;
public class main
{
public static void main(String args[]) throws IOException 
{
   
     //System.out.println("Enter your url or command ");
 BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//String cmd_1=br.readLine();
 String cmd="python ../python_embed/1.py";
        java.util.Scanner s = new java.util.Scanner(Runtime.getRuntime().exec(cmd ).getInputStream()).useDelimiter("\\A");
       System.out.println(s.hasNext() ? s.next() : "");
    }
} 
