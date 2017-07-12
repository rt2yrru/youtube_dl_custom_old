
import java.io.*;
public class main_2
{
public static void main(String args[]) throws IOException 
{
   
     System.out.println("Enter your url or command ");
 BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
String cmd_1=br.readLine();
 String cmd="youtube-dl "+cmd_1;
        java.util.Scanner s = new java.util.Scanner(Runtime.getRuntime().exec(cmd ).getInputStream()).useDelimiter("\\A");
       System.out.println(s.hasNext() ? s.next() : "");
    }
}