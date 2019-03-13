//This is a program to map the acts to the case files
import java.io.*;
import java.util.*;

public class searchActsTXT{

	public static void main(String[] args){

	try{
		FileInputStream fin = new FileInputStream("/home/aadsah/Open_Soft_LLR/2019/OpenSoft-Data/actlist.txt");
		BufferedReader br = new BufferedReader(new InputStreamReader(fin));
		String actline=null;

		PrintWriter out = new PrintWriter("/home/aadsah/Open_Soft_LLR/2019/Act_File_Map.txt");	

		while((actline = br.readLine())!=null){
			out.print(actline);
			final File folder = new File("/home/aadsah/Open_Soft_LLR/2019/OpenSoft-Data/All_FT");
			for(final File file : folder.listFiles()){
				if(file.isFile()){
				
					Scanner scanner = new Scanner(new FileInputStream(file.getPath()));
				
					while(scanner.hasNextLine()){
						if(scanner.nextLine().contains(actline)){
							out.print(", "+file.getName());
							break;
						}
					}				
				}
			}
			out.print("\n");
		}
		fin.close();
		out.close();
		br.close();
	}catch(FileNotFoundException excep){
		System.out.println(excep);
		System.exit(-1);
	}
	catch(IOException exce){
		System.out.println(exce);
		System.exit(-1);
	}
	}
}
