package MainUI;

import java.awt.*;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Date;
import java.sql.SQLException;

import javax.swing.*;

public class Contents_answer extends JFrame implements ActionListener {
	private JButton btn_answer;
	private JTextArea ta_content;
	private DB_Mysql user_DB = new DB_Mysql();
	private ManagerUI managerUI;
	private JTextArea ta_answer;
	
	
	public Contents_answer(ManagerUI managerUI ,String contents,String answer) {
		setTitle("Answer");
		setSize(500,300);
		setLocationRelativeTo(this);
		setLayout(new BorderLayout());
		this.managerUI = managerUI;
		
		ta_content = new JTextArea(3,30);
		JPanel North = new JPanel();
		ta_content.setText(contents);
		North.add(ta_content);
		
		add(North,BorderLayout.NORTH);
		
		ta_answer = new JTextArea(3,20);
		ta_answer.setText(answer);
		add(ta_answer,BorderLayout.CENTER);
		
		btn_answer = new JButton("답변작성");
		add(btn_answer,BorderLayout.SOUTH);
		btn_answer.addActionListener(this);
		user_DB.connectDB();
		setVisible(true);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		Object obj = e.getSource();
		if(obj == btn_answer) {
			
			int input = JOptionPane.showConfirmDialog(this, "답글을 다시겠습니까?? ","Select OptionPane....",JOptionPane.YES_NO_CANCEL_OPTION);
			if (input == 0) {
				user_DB.updateDB(ta_content.getText());
				user_DB.updateAnswer(ta_content.getText(),ta_answer.getText());
				user_DB.selectDB("SELECT * FROM DB.TB");
				managerUI.boardDfTable.setNumRows(0);
				try {
					
					while(user_DB.rs.next()) {
						String id = user_DB.rs.getString("id");
						String title = user_DB.rs.getString("title");
						String content = user_DB.rs.getString("content");
						Date date = user_DB.rs.getDate("date");
						String answer = user_DB.rs.getString("answer");
						String answer_content = user_DB.rs.getString("answer_Content");
						Object data[] = {id,title,content,date,answer,answer_content};
						
						managerUI.boardDfTable.addRow(data);
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
