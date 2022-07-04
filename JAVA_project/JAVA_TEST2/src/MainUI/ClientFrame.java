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
import java.net.Socket;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class ClientFrame extends JPanel implements ActionListener,Runnable{

	private JPanel panelCenter;
	private JPanel panelSouth;
	
	private JTextField tf;
	private JButton btn;
	
	private JTextArea ta;
	
	private Socket socket = null;
	private BufferedReader in = null;
	private BufferedWriter out = null;
	
	public ClientFrame(String title) {


		setLayout(new BorderLayout());
		
		setCenter();
		
		//setSouth();
		
		setVisible(true);
		
		//tf.requestFocus();
	}

	private void setCenter() {
		panelCenter = new JPanel();
		//panelCenter.setBackground(new Color(136,141,200));
		
		ta = new JTextArea(20, 35);
		ta.append("----------------------------------------------------");
		ta.setLineWrap(true);
		ta.setEditable(false);
		JScrollPane sp = new JScrollPane(ta,
				JScrollPane.VERTICAL_SCROLLBAR_ALWAYS,
				JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
		panelCenter.add(sp);
		
		add(panelCenter, BorderLayout.CENTER);
	}

	private void setSouth() {
		panelSouth = new JPanel();
		//panelSouth.setBackground(Color.RED);
		
		tf = new JTextField(25);
		tf.addActionListener(this);
		panelSouth.add(tf);
		
		btn = new JButton("전송");
		btn.addActionListener(this);
		panelSouth.add(btn);
		
		add(panelSouth, BorderLayout.SOUTH);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		Object obj = e.getSource();
		
		if(obj == btn || obj == tf) {
			try {
				String outMessage = tf.getText();
				out.write(outMessage + "\n");
				out.flush();
				
				//ta.append(" [클라이언트] : " + outMessage + "\n");
				tf.setText("");
				tf.requestFocus();
			} catch (IOException e1) {
				e1.printStackTrace();
			}
		}
		
	}
	


	public void setSocket() {
		
	}

	@Override
	public void run() {
		try {
			socket = new Socket("localhost", 8888);
			ta.append("서버 연결됨\n");
			
			
			
			in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
			out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
			
			while(true) {
				
				String inMessage = in.readLine();
				if(inMessage.equals("exit")) {
					break;
				}
				ta.append(inMessage + "\n");
			}
			
			
		} catch (IOException e) {
			e.printStackTrace();
		}finally {
			try {
				socket.close();
				out.close();
				in.close();
				
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		
	}
}

