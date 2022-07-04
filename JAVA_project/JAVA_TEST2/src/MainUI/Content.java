package MainUI;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Content extends JFrame  {
	private JButton btn_answer;
	private JTextArea ta_content;
	private DB_Mysql user_DB = new DB_Mysql();
	public Content(String contents,String answer) {
		setTitle("Answer");
		setSize(500,300);
		setLocationRelativeTo(this);
		setLayout(new BorderLayout());
		
		
		ta_content = new JTextArea(3,30);
		String ques = "<========[질문]";
		ta_content.append(ques);
		ta_content.setEditable(false);
		JPanel North = new JPanel();
		ta_content.setText(contents);
		North.add(ta_content);
		add(North,BorderLayout.NORTH);
		
		JTextArea ta_answer = new JTextArea(3,20);
		ta_answer.setText(answer);
		String ans;
		ans = "<========[답변]";
		ta_answer.append(ans);
		ta_answer.setEditable(false);
		add(ta_answer,BorderLayout.CENTER);
		

		setVisible(true);
	}


}
