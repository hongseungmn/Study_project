package MainUI;
//2022-05-26 멀티채팅

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.util.ArrayList;

public class ServerThread extends Thread {
	private Socket socket;
	private ArrayList<ServerThread> list;
	private BufferedReader in;
	private BufferedWriter out;
	public ServerFrame serverFrame;
	
	public ServerThread(Socket socket, ArrayList<ServerThread> list,ServerFrame serverFrame) {
		this.socket = socket;
		this.list = list;
		this.serverFrame = serverFrame;
		
		
		
	}

	@Override
	public void run() {
		try {
			String connIp = socket.getInetAddress().getHostAddress();
			System.out.println(connIp);
			in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
			out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
			
			String inMsg = null;
			
			
			while(true) {
				inMsg = in.readLine();
				
				sendToAllClients(inMsg);
				
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	
	}

	public void sendToAllClients(String outMsg) {
		for(ServerThread st : list) {
		try {
			st.out.write("[ 공지 ] : " + outMsg + "\n");
			st.out.flush(); 
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			
			try {
				if(outMsg.equals("exit"))
				{
					out.close();
					in.close();
					
				}
				
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		}
		serverFrame.getTa().append(outMsg+"\n");
	}
	
}
