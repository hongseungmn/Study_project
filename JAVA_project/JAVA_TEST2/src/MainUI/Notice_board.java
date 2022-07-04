package MainUI;


import java.awt.BorderLayout;


import java.awt.*;
import java.awt.event.*;
import java.sql.*;
import java.time.*;
import java.time.format.DateTimeFormatter;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;


import com.mysql.cj.xdevapi.Statement;

//mysql -h127.0.0.1 -uconnectuser -p connectdb
//CREATE USER 'connectuser'@'%' IDENTIFIED BY 'connect123!@#';
//GRANT ALL PRIVILEGES ON *.* TO 'connectuser'@'%' WITH GRANT OPTION;
//GRANT ALL PRIVILEGES ON connectdb.* to 'connectuser'@'%' WITH GRANT OPTION;
//flush privileges;



public class Notice_board extends JFrame implements ActionListener {
	private JButton write_upload;
	private JTextField write_title;
	private JTextArea write_content;
	private MainUI mainUI;
	public String userId;
	private String pw;
	private String title;
	private String content;
	private String date;
	private DB_Mysql userDB = new DB_Mysql();
	
	
	
	public Notice_board(MainUI mainUI) {
		
		setTitle("Notice_board");
		setSize(400,400);
		this.mainUI = mainUI;
		userId = mainUI.userId;
		setResizable(false);
		setLocationRelativeTo(this);
		Container c = getContentPane();
		c.setLayout(new BorderLayout());
		
		JPanel Center = new JPanel();
		write_content = new JTextArea(15,30);
		Center.add(write_content);
		
		JPanel North = new JPanel();
		JLabel write_title_label = new JLabel("제목 : ");
		write_title = new JTextField(15);
		North.add(write_title_label);
		North.add(write_title);
		
		JPanel South = new JPanel();
		write_upload = new JButton("게시");
		write_upload.addActionListener(this);
		South.add(write_upload);
		
		
		

		add(North,BorderLayout.NORTH);
		add(Center,BorderLayout.CENTER);
		add(South,BorderLayout.SOUTH);
		userDB.connectDB();
		setVisible(true);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		Object obj = e.getSource();
		if(obj == write_upload) {
			
			int input = JOptionPane.showConfirmDialog(this, "정말 게시하시겠습니까?? ","Select OptionPane....",JOptionPane.YES_NO_CANCEL_OPTION);
			
			if(input == 0) {

				String id = userId;
				title = write_title.getText();
				content = write_content.getText();
				LocalDate now = LocalDate.now();
				DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
				String date = now.format(formatter);
				Object data[] = {id,title,content,date};
				mainUI.notice_table.addRow(data);
				userDB.insertDB(id, title, content,date);
				userDB.selectDB("SELECT * FROM DB.TB");
				mainUI.notice_table.setNumRows(0);
				try {
					
					while(userDB.rs.next()) {
						String id_update = userDB.rs.getString("id");
						String title_update = userDB.rs.getString("title");
						String content_update = userDB.rs.getString("content");
						Date date_update = userDB.rs.getDate("date");
						String answer_update = userDB.rs.getString("answer");
						Object data_update[] = {id_update,title_update,content_update,date_update,answer_update};
						
						mainUI.notice_table.addRow(data_update);
					}
				} catch (SQLException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				
				dispose();
			}
			else if(input == 1) {
				dispose();
			}
			
			
			
			
	
		}
		
	}
	
	
	

	

	
	
	
}
