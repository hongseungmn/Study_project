package MainUI;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTabbedPane;
import javax.swing.JTextArea;
import javax.swing.*;

import java.awt.*;

public class MainUI extends JFrame {
	public MainUI() {
		setTitle("MainUI");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(1000,800);
		setLocationRelativeTo(this);
		setLayout(new BorderLayout());
		
		JTabbedPane TP = new JTabbedPane();
		
		JPanel North = new JPanel();
		JTextArea North_Tap = new JTextArea(2,50);
		North.add(North_Tap);
		add(North,BorderLayout.NORTH);
		
		
		JPanel tab1 = new JPanel();
		JPanel tab2 = new JPanel();
		JPanel tab3 = new JPanel();
		JTextArea tab3_help = new JTextArea(50,80);
		tab3.add(tab3_help);
		
		
		
		tab2.setLayout(new FlowLayout());
		
		JPanel search_panel = new JPanel();
		JLabel search = new JLabel("검색");
		
		
		String search_list[] = {"test1","test2","test3","test4","test5"};
		JComboBox<String> search_com;
		search_com = new JComboBox<String>(search_list);
		
		JTextField search_tf = new JTextField(10);
		JButton search_btn = new JButton("search");
		
		search_panel.setBackground(Color.GRAY);
		search_panel.add(search);
		search_panel.add(search_com);
		search_panel.add(search_tf);
		tab2.add(search_panel);
		
		
		
		
		TP.add("Show ",tab1);
		TP.add("게시판",tab2);
		TP.add("도움말",tab3);
		add(TP,BorderLayout.CENTER);
		
		setVisible(true);
		
	}
	public static void main(String[] args) {
		new MainUI();
	}
}
