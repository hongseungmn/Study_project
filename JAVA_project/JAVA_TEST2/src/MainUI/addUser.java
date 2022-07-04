package MainUI;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class addUser extends JFrame implements ActionListener {
	private JTextField id;
	private JTextField pw;
	private JTextField email;
	private JButton addCheck;
	private DB_Mysql useDB = new DB_Mysql();
	private ManagerUI managerUI;
	
	public addUser(ManagerUI managerUI) {
		setTitle("add User");
		setSize(300,250);
		setLocationRelativeTo(this);
		setLayout(new BorderLayout());
		this.managerUI = managerUI;
		
		JPanel inputText = new JPanel();
		inputText.setLayout(new GridLayout(6,2));
		id = new JTextField(10);
		pw = new JTextField(10);
		email = new JTextField(10);
		inputText.add(new JLabel(" 아이디"));
		inputText.add(id);
		inputText.add(new JPanel());
		inputText.add(new JPanel());
		inputText.add(new JLabel(" 비밀번호"));
		inputText.add(pw);
		inputText.add(new JPanel());
		inputText.add(new JPanel());
		inputText.add(new JLabel("이름"));
		inputText.add(email);
		inputText.add(new JPanel());
		inputText.add(new JPanel());
		
		addCheck = new JButton("추가");
		addCheck.addActionListener(this);
		
		add(inputText,BorderLayout.CENTER);
		add(addCheck,BorderLayout.SOUTH);
		
		
		setVisible(true);
		useDB.connectDB();
		
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		
		Object obj = e.getSource();
		if(obj == addCheck) {
			int result = JOptionPane.showConfirmDialog(null, "아이디 : "+ id.getText() +"\n 비밀번호 : "+ pw.getText() +"\n 이름 : "+email.getText() + "\n 계속하시겠습니까?","Confirm",JOptionPane.YES_NO_OPTION);
			if(result == JOptionPane.YES_OPTION) {
				useDB.insertUser(id.getText(), pw.getText(), email.getText());
				managerUI.userTableSet();
				dispose();
			}
			else
				dispose();
			
		}
		
	}

}
