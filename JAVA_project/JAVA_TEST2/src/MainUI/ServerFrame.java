package MainUI;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class ServerFrame extends JFrame implements ActionListener,Runnable{

	private JPanel panelNorth;
	private JPanel panelCenter;
	private JPanel panelSouth;
	private JTextField tf;
	private JButton btn;	
	private JTextArea ta;
	private JTextArea edit;
	private ServerSocket server = null;
	private ArrayList<ServerThread> list = new ArrayList<>();
	public ClientFrame clientFrame;
	public ServerThread st;
	public ServerFrame(String title) {
		
		setLocation(1250, 320);
		setSize(400,600);
		setLayout(new BorderLayout());
		setResizable(false);
		setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
		setNorth();
		
		setCenter();
		
		setVisible(true);
		
	}


	private void setNorth() {
		panelNorth = new JPanel();
		panelNorth.setLayout(new BorderLayout());
		panelNorth.setBackground(Color.BLUE);
		
		ta = new JTextArea(7, 5);
		ta.setLineWrap(true);
		ta.setEditable(false);
		JScrollPane sp = new JScrollPane(ta,
				JScrollPane.VERTICAL_SCROLLBAR_ALWAYS,
				JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
		panelNorth.add(sp);
		
		add(panelNorth, BorderLayout.NORTH);
	}

	private void setCenter() {
		panelCenter = new JPanel();
		panelSouth = new JPanel();
		edit = new JTextArea(7,15);
		edit.setLineWrap(true);
		edit.setEditable(false);
		JScrollPane sp2 = new JScrollPane(edit,
				JScrollPane.VERTICAL_SCROLLBAR_ALWAYS,
				JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
		//panelCenter.add(sp2);
		add(sp2,BorderLayout.CENTER);
		
		
		tf = new JTextField(20);
		tf.addActionListener(this);
		panelSouth.add(tf);
		btn = new JButton("전송");
		btn.addActionListener(this);
		panelSouth.add(btn);
		
		add(panelSouth, BorderLayout.SOUTH);
		
		
	}





	public void setServer() {
		
	}

	public JTextArea getTa() {
		return edit;
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		Object obj = e.getSource();
		if(obj == btn || obj == tf) {
			String text = tf.getText();
			st.sendToAllClients(text);
			tf.setText("");
		}
		
	}


	@Override
	public void run() {
		try {
			server  = new ServerSocket(8888);
			ta.append(" >>> 연결 대기중... \n");
			
			while(true) {
				//접속이 될때마다 소켓이 연결된 것을 알려줌
				Socket socket = server.accept();
				ta.append(">> 클라이언트 연결됨 \n");
				st = new ServerThread(socket, list,this);
				list.add(st);
				st.start();
			}
			
		} catch (IOException e) {
			e.printStackTrace();
		}finally {
			try {
				//socket.close();
				server.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		
	}
}