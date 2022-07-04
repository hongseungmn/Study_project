package MainUI;

import javax.swing.*;


import MainUI.HintTextField;
import MainUI.MainUI.ImagePanel;
import videoUI.PasswordHintTextField;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import java.sql.SQLException;
import java.util.concurrent.CountDownLatch;

public class Login extends JFrame implements ActionListener, FocusListener {
	public DB_Mysql useDB = new DB_Mysql();
	private HintTextField email;
	private PasswordHintTextField pw;
	private HintTextField id;
	private String userPw;
	private String userId;
	public int userIndex;
	private Image chimg;
	private RoundButton loginButton;
	private RoundButton FixButton;
	
	
	public Login() {
		setTitle("Login");
		setSize(400,500);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLocationRelativeTo(this);
		setBackground(Color.WHITE);
		setLayout(null);
		setResizable(false);
		
		ImageIcon LoginImage = new ImageIcon("src/img/back.jpg");
		
		Image image = LoginImage.getImage();
		chimg = image.getScaledInstance(400, 500, 200);
		ImageIcon LoginImagech = new ImageIcon(chimg);
		
		ImagePanel login = new ImagePanel(LoginImagech.getImage());
		
		login.setLayout(null);
		login.setBounds(0, 0, 400, 500);
		
		ImageIcon logo = new ImageIcon("src/img/inhatube2.png");
		
		Image chlogo = logo.getImage();
		chimg = chlogo.getScaledInstance(380, 100, 200);
		ImageIcon logoch = new ImageIcon(chimg);
		
		JLabel logoLabel = new JLabel(logoch);
		logoLabel.setBounds(20, 30, 350, 120);
		login.add(logoLabel);
		
		JLabel codelabel = new JLabel("이름");
		codelabel.setBounds(85, 140, 50, 25);
		codelabel.setFont(new Font("D2Coding", Font.BOLD, 14));
		
		JLabel idlabel = new JLabel("아이디");
		idlabel.setBounds(85, 190, 50, 25);
		idlabel.setFont(new Font("D2Coding", Font.BOLD, 14));
		
		JLabel passlabel = new JLabel("비밀번호");
		passlabel.setBounds(85, 240, 60, 25);
		passlabel.setFont(new Font("D2Coding", Font.BOLD, 14));
		
		email = new HintTextField("이름");
		email.addActionListener(this);
		email.setBounds(85, 165, 200, 25);
		
		id = new HintTextField("제공받은 ID");
		id.addActionListener(this);
		id.setBounds(85, 215, 200, 25);
		
		pw = new PasswordHintTextField("제공받은 PW");
		pw.addActionListener(this);
		pw.setBounds(85, 265, 200, 25);
		
		
		login.add(codelabel);
		login.add(idlabel);
		login.add(passlabel);
		login.add(id);
		login.add(pw);
		login.add(email);
		
		
		loginButton = new RoundButton("로그인");
		loginButton.setBounds(90, 310, 90, 30);
		loginButton.setFont(new Font("D2Coding", Font.BOLD, 14));
		loginButton.addActionListener(this);
		FixButton = new RoundButton("수강 신청");
		FixButton.setBounds(190, 310, 90, 30);
		FixButton.setFont(new Font("D2Coding", Font.BOLD, 14));
		
		login.add(loginButton);
		login.add(FixButton);
		
		add(login);
		
		useDB.connectDB();
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new Login();
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		Object obj = e.getSource();
		if(obj == loginButton || obj == pw || obj == id) {
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
					
					managerMain.setVisible(true);
				}
				else {
					System.out.println("userId : " + userId);
					System.out.println("userPw : " + userPw);
					System.out.println("로그인 되셨습니다");
					
					int input = JOptionPane.showConfirmDialog(this,"로그인 정보를 확인하세요.\n" +
							"이름 : " + getEmail + "\n" +
							"아이디 : " + getId ,"로그인 성공",JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
					if (input == 0) {
						JFrame userMain =  new MainUI(userId,userIndex);
						setVisible(false);
					}
				}
				
				
			}
			else {
				JOptionPane.showMessageDialog(this,"회원정보가 존재하지 않습니다","로그인",JOptionPane.ERROR_MESSAGE);
				id.setText("제공받은 ID");
				pw.setText("제공받은 PW");
				email.setText("이름");
				
				id.setFont(new Font("Gothic", Font.PLAIN, 12));
				pw.setFont(new Font("Gothic", Font.PLAIN, 12));
				email.setFont(new Font("Gothic", Font.PLAIN, 12));
				
				id.setForeground(Color.GRAY);
				pw.setForeground(Color.GRAY);
				email.setForeground(Color.GRAY);
			}
		} catch (SQLException e1) {
			
			e1.printStackTrace();
		} finally {
		}
		}
		else if (obj == FixButton) {
			
		}
		
	}

	@Override
	public void focusGained(FocusEvent e) {
		Object obj = e.getSource();
	}

	@Override
	public void focusLost(FocusEvent e) {
		Object obj = e.getSource();
	}
	class ImagePanel extends JPanel {

		  private Image img;

		  public ImagePanel(String img) {
		    this(new ImageIcon(img).getImage());
		  }

		  public ImagePanel(Image img) {
		    this.img = img;
		    Dimension size = new Dimension(img.getWidth(null), img.getHeight(null));
		    setPreferredSize(size);
		    setMinimumSize(size);
		    setMaximumSize(size);
		    setSize(size);
		    setLayout(null);
		  }

		  public void paintComponent(Graphics g) {
		    g.drawImage(img, 0, 0, null);
		  }
	}
}
