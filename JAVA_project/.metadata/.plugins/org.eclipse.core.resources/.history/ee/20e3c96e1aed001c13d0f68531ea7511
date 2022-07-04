package MainUI;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.sql.Date;
import java.sql.SQLException;

import javax.swing.table.DefaultTableModel;

import videoUI.VideoManager;


public class ManagerUI extends JFrame implements ActionListener, WindowListener {
	public DefaultTableModel userDfTable;
	public DefaultTableModel boardDfTable;
	private JButton board_update;
	private JButton board_delete;
	private JButton user_update;
	private JButton user_delete;
	public DB_Mysql useDB = new DB_Mysql(); 
	public JTable userTable;
	public JTable boardTable;
	public ServerFrame sf;
	public ClientFrame clientFrame;
	public VideoManager videotest = new VideoManager();
	public ManagerUI() {
		
		setTitle("ManagerGUI");
		setSize(800,800);
		setLocationRelativeTo(this);
		setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
		setLayout(new BorderLayout());
		setResizable(false);
		addWindowListener(this);
		
		
		JTabbedPane managerPane = new JTabbedPane();
		JPanel tab1 = new JPanel();
		tab1.setLayout(new BorderLayout());
		JPanel tab2 = new JPanel();
		tab2.setLayout(new BorderLayout());
		
		
		
		//tab1
		
		
		String userHeader[] = new String[] {"Index","아이디","비밀번호","이름"}; 
		
		userDfTable = new DefaultTableModel(userHeader,0) {
			public boolean isCellEditable(int i, int c) {
				return false;
			} 
		};
		
		userTable = new JTable(userDfTable);	
		userTable.setRowHeight(25);
		userTable.getTableHeader().setReorderingAllowed(false);
		userTable.getTableHeader().setResizingAllowed(false);
		userTable.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
		userTable.setPreferredScrollableViewportSize(new Dimension(700,600));
		userTable.setFillsViewportHeight(true);
		VideoTableRender table_rander1 = new VideoTableRender("user",1);
		userTable.setDefaultRenderer(Object.class, table_rander1);
		
		JScrollPane scrollPane = new JScrollPane(userTable);
		JPanel tab1_center = new JPanel();
		tab1_center.add(scrollPane);
		
		JPanel tab1_Bottom = new JPanel();
		tab1_Bottom.setLayout(new FlowLayout());
		user_update = new JButton("회원 추가");
		user_update.addActionListener(this);
		user_delete = new JButton("회원 삭제");
		user_delete.addActionListener(this);
		tab1_Bottom.add(user_update);
		tab1_Bottom.add(user_delete);
		
		tab1.add(tab1_Bottom,BorderLayout.SOUTH);
		tab1.add(tab1_center,BorderLayout.CENTER);
		
		
		
		
		//tab2
		String boardHeader[] = new String[] {"id","title","Content","Date","answer","answer_content"}; 
		
		boardDfTable = new DefaultTableModel(boardHeader,0) {
			public boolean isCellEditable(int i, int c) {
				return false;
			} 
		};
		
		boardTable = new JTable(boardDfTable);	
		boardTable.setRowHeight(25);
		boardTable.getTableHeader().setReorderingAllowed(false);
		boardTable.getTableHeader().setResizingAllowed(false);
		boardTable.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
		boardTable.setPreferredScrollableViewportSize(new Dimension(700,600));
		boardTable.setFillsViewportHeight(true);
		TableRender table_rander = new TableRender();
		boardTable.setDefaultRenderer(Object.class, table_rander);
		JScrollPane scrollPane2 = new JScrollPane(boardTable);
		JPanel tab2_center = new JPanel();
		tab2_center.add(scrollPane2);
		
		JPanel tab2_Bottom = new JPanel();
		tab2_Bottom.setLayout(new FlowLayout());
		board_update = new JButton("답글 작성");
		board_update.addActionListener(this);
		board_delete = new JButton("게시물 삭제");
		board_delete.addActionListener(this);
		
		tab2_Bottom.add(board_update);
		tab2_Bottom.add(board_delete);
		
		tab2.add(tab2_Bottom,BorderLayout.SOUTH);
		tab2.add(tab2_center,BorderLayout.CENTER);
		
		
		//graph1
		JPanel graph_time = new JPanel();
		JPanel userGraph = new JPanel();
		GraphUser userStudyGraph = new GraphUser("회원 공부 현황");
		userGraph.add(userStudyGraph.chartPanel);
		userGraph.setBorder(BorderFactory.createLineBorder(Color.black,5));
		graph_time.add(userGraph);
		
		//graph2 -java
		JPanel graph2 = new JPanel();
		
		
		graph2.setLayout(new BoxLayout(graph2,BoxLayout.Y_AXIS));
		graph2.setBorder(BorderFactory.createEmptyBorder(30 , 0 , 30 , 0));
				
		JPanel userGraph1 = new JPanel();
		GraphUser2 JavaGraph = new GraphUser2("JAVA",new Color(200,50,0));
		userGraph1.add(JavaGraph.chartPanel);
		userGraph1.setBorder(BorderFactory.createLineBorder(Color.black,5));
		graph2.add(userGraph1);
		
		//graph2 -c
		JPanel userGraph2 = new JPanel();
		GraphUser2 cGraph = new GraphUser2("C",new Color(144,32,123));
		userGraph2.add(cGraph.chartPanel);
		userGraph2.setBorder(BorderFactory.createLineBorder(Color.black,5));
		graph2.add(userGraph2);
		
		//graph2 -node_js
		JPanel userGraph3 = new JPanel();
		GraphUser2 nodeGraph = new GraphUser2("Node_js",new Color(0,255,255));
		userGraph3.add(nodeGraph.chartPanel);
		userGraph3.setBorder(BorderFactory.createLineBorder(Color.black,5));
		graph2.add(userGraph3);
		
		//graph2 -Python
		JPanel userGraph4 = new JPanel();
		GraphUser2 pythonGraph = new GraphUser2("Python",new Color(0,0,255));
		userGraph4.add(pythonGraph.chartPanel);
		userGraph4.setBorder(BorderFactory.createLineBorder(Color.black,5));
		graph2.add(userGraph4);
		
		//graph2 -scratch
		JPanel userGraph5 = new JPanel();
		GraphUser2 scratchGraph = new GraphUser2("Scratch",new Color(0,255,0));
		userGraph5.add(scratchGraph.chartPanel);
		userGraph5.setBorder(BorderFactory.createLineBorder(Color.black,5));
		graph2.add(userGraph5);
		
		//graph2 -arduino
		JPanel userGraph6 = new JPanel();
		GraphUser2 arduinoGraph = new GraphUser2("Arduino",new Color(255,255,0));
		userGraph6.add(arduinoGraph.chartPanel);
		userGraph6.setBorder(BorderFactory.createLineBorder(Color.black,5));
		graph2.add(userGraph6);
		
		JScrollPane graph2_scroll = new JScrollPane(graph2,JScrollPane.VERTICAL_SCROLLBAR_ALWAYS,JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
		
		
		
		
	
		
		
		//tab4 동영상 관리
		JPanel videoManager = new JPanel();
		videoManager.add(videotest.video);
		
		
		
		managerPane.addTab("회원 공부 현황",graph_time);
		managerPane.addTab("회원 공부 진행율", graph2_scroll);
		managerPane.addTab("회원 관리",tab1);
		managerPane.addTab("게시판 관리",tab2);
		managerPane.addTab("동영상 관리", videoManager);
		
		
		add(managerPane);
		
		
		
		
		setVisible(true);
		useDB.connectDB();
		userTableSet();
		boardTableSet();
		
		sf = new ServerFrame("SERVER");
		Thread th = new Thread(sf);
		th.start();
		
		

		
		
		
		
	}
	private void boardTableSet() {
		boardDfTable.setNumRows(0);
		useDB.selectDB("SELECT * FROM DB.TB");
		try {
			System.out.println("Query OK");
			while(useDB.rs.next()) {
				String userId = useDB.rs.getString("id");
				String title = useDB.rs.getString("title");
				String Content = useDB.rs.getString("Content");
				Date date = useDB.rs.getDate("Date");
				String answer = useDB.rs.getString("answer");
				String answer_content = useDB.rs.getString("answer_Content");
				Object data[] = {userId,title,Content,date,answer,answer_content};
				boardDfTable.addRow(data);
			}
		} catch(SQLException e) {
			
			e.printStackTrace();
		}
		
	}
	
	
	public void userTableSet() {
		userDfTable.setNumRows(0);
		useDB.selectDB("SELECT * FROM DB.USER");
		try {
			System.out.println("Query OK");
			while(useDB.rs.next()) {
				
				int index = useDB.rs.getInt("index");
				String userId = useDB.rs.getString("id");
				String userPw = useDB.rs.getString("PW");
				String userName = useDB.rs.getString("userName");
				Object data[] = {index,userId,userPw,userName};
				userDfTable.addRow(data);
			}
		} catch (SQLException e) {
		
			e.printStackTrace();
		}
		
	}
	public static void main(String[] args) {
		new ManagerUI();
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		
		Object obj = e.getSource();
		
		if(obj == board_update) {
			
			int ques_row = boardTable.getSelectedRow();
			String content = (String) boardTable.getValueAt(ques_row, 2);
			String answer = (String) boardTable.getValueAt(ques_row, 5);
			new Contents_answer(this,content,answer);
		}
		else if(obj == board_delete) {
			
			int input = JOptionPane.showConfirmDialog(this, "게시글을 삭제하시겠습니까?? ","Select OptionPane....",JOptionPane.YES_NO_CANCEL_OPTION);
			if (input == 0) {
				int ques_row = boardTable.getSelectedRow();
				String title = (String) boardTable.getValueAt(ques_row, 1);
				String content = (String) boardTable.getValueAt(ques_row, 2);
				useDB.deleteBoard(title,content);
				boardDfTable.setNumRows(0);
				
				try {
					useDB.selectDB("SELECT * FROM DB.TB");
					while(useDB.rs.next()) {
						String id2 = useDB.rs.getString("id");
						String title2 = useDB.rs.getString("title");
						String content2 = useDB.rs.getString("content");
						Date date2 = useDB.rs.getDate("date");
						String answer2 = useDB.rs.getString("answer");
						String answer_content2 = useDB.rs.getString("answer_Content");
						Object data[] = {id2,title2,content2,date2,answer2,answer_content2};
						
						boardDfTable.addRow(data);
					}
				} catch (SQLException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
			}
			else if(input == 1) {
				
			}
		}
		else if(obj == user_update) {
			new addUser(this);
		}
		else if(obj ==user_delete) {
			int row = userTable.getSelectedRow();
			int index = (int) userTable.getValueAt(row, 0);
			useDB.deleteUser(index);
			userTableSet();
		}
	}
	@Override
	public void windowOpened(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void windowClosing(WindowEvent e) {
		int k = JOptionPane.showConfirmDialog(null, "프로그램을 종료하시겠습니까? ","종료",JOptionPane.OK_CANCEL_OPTION,JOptionPane.INFORMATION_MESSAGE);
		
		if(k == 0) {
			System.exit(0);
		}
		else if(k == 2){
			
		}
		
	}
	@Override
	public void windowClosed(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void windowIconified(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void windowDeiconified(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void windowActivated(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void windowDeactivated(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}
	
	
}
