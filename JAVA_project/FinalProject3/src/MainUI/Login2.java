package MainUI;

import javax.swing.*;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;

public class Login2 extends JFrame implements ActionListener {
	public DB_Mysql useDB = new DB_Mysql();
	private JTextField email;
	private JTextField pw;
	private JTextField id;
	private String userPw;
	private String userId;
	private JFrame userMain;
	public int userIndex;
	
	
	public Login2() {
		setTitle("Login");
		setSize(300,300);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setResizable(false);
		setLocationRelativeTo(this);
		setLayout(new BorderLayout());
		JPanel loginMain = new JPanel();
		loginMain.setLayout(new GridLayout(3,2));
		
		id = new JTextField(10);
		pw = new JTextField(10);
		email = new JTextField(10);
		loginMain.add(new JLabel(" 아이디"));
		loginMain.add(id);
		loginMain.add(new JLabel(" 비밀번호"));
		loginMain.add(pw);
		loginMain.add(new JLabel(" 이메일"));
		loginMain.add(email);
		
		JPanel loginBottom = new JPanel();
		loginBottom.setLayout(new FlowLayout());
		
		JButton loginButton = new JButton("로그인");
		loginButton.addActionListener(this);
		JButton joinButton = new JButton("회원가입");
		
		loginBottom.add(loginButton);
		loginBottom.add(joinButton);
		
		add(loginMain,BorderLayout.CENTER);
		add(loginBottom,BorderLayout.SOUTH);
		
		useDB.connectDB();
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new Login2();
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		String getId = id.getText();
		String getPw = pw.getText();
		String getEmail = email.getText();
		
		String sql = "SELECT * FROM DB.`USER` WHERE id='" + getId + "'AND pw='" + getPw + "'";
		useDB.login_selectDB(sql);
		System.out.println(sql);
		try {
			System.out.println("Query OK");
			if(useDB.rs.next()) {
				userId = useDB.rs.getString("id");
				userPw = useDB.rs.getString("pw");
				userIndex = useDB.rs.getInt("index");
				System.out.println(userIndex);
				if(userId.equals("manager") && userPw.equals("manager1234")) {
					System.out.println("userId : " + userId);
					System.out.println("userPw : " + userPw);
					System.out.println("관리자 로그인입니다.");
					JFrame managerMain = new ManagerUI();
					
				}
				else {
					System.out.println("userId : " + userId);
					System.out.println("userPw : " + userPw);
					System.out.println("로그인 되셨습니다");
					
					userMain =  new MainUI(userId,userIndex);
					
					
				}
				
				
			}
			else {
				JOptionPane.showMessageDialog(null,"회원정보가 존재하지 않습니다","로그인",JOptionPane.ERROR_MESSAGE);
				System.out.println("회원정보가 없습니다");
				id.setText("");
				pw.setText("");
				email.setText("");
				
			}
		} catch (SQLException e1) {
			
			e1.printStackTrace();
		}
		
		dispose();
		
	}
}
