package videoUI;

import java.awt.BorderLayout;


import java.awt.Color;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.sql.Date;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.ListSelectionModel;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableModel;


import MainUI.VideoTableRender;
import videoUI.DB_Video;


public class VideoManager extends JFrame implements ActionListener, MouseListener{

	private JTable main_Board;
	private DefaultTableModel notice_table;
	private DefaultTableCellRenderer celTextCenter;
	private DefaultTableCellRenderer celTextLeft;
	private DefaultTableCellRenderer celTextRight;
	private DefaultTableCellRenderer celTextColor;
	private JPanel JavaPanel;
	
	private JComboBox<String> search_com;
	private JTextField search_tf;
	private JButton searchBtn;
	private JButton refleshBtn;
	private String[] url;
	private JComboBox<String> search_cat;
	private JButton uploadBtn;
	private JButton deleteBtn;
	public JPanel video;
	public VideoManager() {
		
		//setBackground(Color.orange);
		
		DB_Video.init();
		
//		데이터베이스 행개수 구하기위해 
		ResultSet rs= DB_Video.getResult("select * from DB.video_java");
		int urltotal = 0;
		try {
			while(rs.next()) {
				urltotal++;
			}
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			try {
				rs.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
//		url 주소 입력
		url = new String[urltotal];
		ResultSet rs1= DB_Video.getResult("select * from DB.video_java");
		int i = 0;
		try {
			while(rs1.next()) {
				try {
					url[i] = rs1.getString("url");
					i++;
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			try {
				rs1.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		
		
		video = new JPanel();
		video.setLayout(new BorderLayout());
		
		JPanel search_panel = new JPanel();
		JPanel south_panel = new JPanel();
		JPanel video_content = new JPanel();
		
		String search_list[] = {"Title", "Content", "Num"};
		String categori_list[] = {"JAVA", "C", "ARDUINO", "PYTHON", "SCRATCH", "NODE.JS"};
		search_com = new JComboBox<String>(search_list);
		search_cat = new JComboBox<String>(categori_list);
		search_cat.addActionListener(this);
		
		search_tf = new JTextField(23);
		search_tf.addActionListener(this);
		
		searchBtn = new JButton("검색");
		searchBtn.addActionListener(this);
		refleshBtn = new JButton("새로고침");
		refleshBtn.addActionListener(this);
		
		search_panel.add(search_cat);
		search_panel.add(search_com);
		search_panel.add(search_tf);
		search_panel.add(searchBtn);
		search_panel.add(refleshBtn);
		
		video.add(search_panel, BorderLayout.NORTH);
		
		uploadBtn = new JButton("업로드");
		uploadBtn.addActionListener(this);
		deleteBtn = new JButton("삭제");
		deleteBtn.addActionListener(this);
		
		south_panel.add(uploadBtn);
		south_panel.add(deleteBtn);
		
		video.add(south_panel, BorderLayout.SOUTH);
		
		String header[] = new String[] {"Num","Content","Title","Date","조회수"};
		
		notice_table = new DefaultTableModel(header,0) {
			public boolean isCellEditable(int i, int c) {
				return false;
			} 
		};
		
		main_Board = new JTable(notice_table);
		
		
		
//		celTextCenter = new DefaultTableCellRenderer();
//		celTextLeft = new DefaultTableCellRenderer();
//		celTextRight = new DefaultTableCellRenderer();
//		celTextColor = new DefaultTableCellRenderer();
//		celTextCenter.setHorizontalAlignment(JLabel.CENTER);
//		celTextLeft.setHorizontalAlignment(JLabel.LEFT);
//		celTextRight.setHorizontalAlignment(JLabel.RIGHT);
//		celTextColor.setForeground(Color.red);
//		
//		main_Board.getColumn("Title").setCellRenderer(celTextLeft);
//		main_Board.getColumn("Content").setCellRenderer(celTextCenter);
//		main_Board.getColumn("Date").setCellRenderer(celTextCenter);
//		main_Board.getColumn("조회수").setCellRenderer(celTextCenter);
//		main_Board.getColumn("Num").setCellRenderer(celTextCenter);
		
		
		
		main_Board.setRowHeight(25);
		main_Board.getColumn("Num").setPreferredWidth(30);
		main_Board.getColumn("Content").setPreferredWidth(50);
		main_Board.getColumn("Title").setPreferredWidth(170);
		main_Board.getColumn("Date").setPreferredWidth(80);
		main_Board.getColumn("조회수").setPreferredWidth(30);
		VideoTableRender table_rander = new VideoTableRender("asd",1);
		
		main_Board.getTableHeader().setReorderingAllowed(false);
		main_Board.getTableHeader().setResizingAllowed(false);
		main_Board.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
		main_Board.setPreferredScrollableViewportSize(new Dimension(700,550));
		main_Board.setFillsViewportHeight(true);
		main_Board.setDefaultRenderer(Object.class, table_rander);
		main_Board.addMouseListener(this);
		JScrollPane scrollPane = new JScrollPane(main_Board);
		video_content.add(scrollPane);
		video.add(scrollPane);
		//add(video, BorderLayout.CENTER);
		
		JavaPanel = new JPanel();
		JavaPanel.setLayout(new BorderLayout());
		
		notice_table.setNumRows(0);
		ResultSet rs2= DB_Video.getResult("select * from DB.video_java");
		
		try {	
			while(rs2.next()) {
					int num = rs2.getInt("num");
					String videoname = rs2.getString("content");
					String videourl = rs2.getString("title");
					Date date = rs2.getDate("date");
					int 조회수 = rs2.getInt("조회수");
				
					Object data[] = {num,videoname,videourl,date,조회수};
					notice_table.addRow(data);
				}
			} catch (SQLException e1) {
				e1.printStackTrace();
			} finally {
				try {
					rs2.close();
				} catch (SQLException e1) {
					e1.printStackTrace();
				}
			}
		
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		Object obj = e.getSource();
		if(obj == search_cat){
			String sql = "";
			String cat = "VIDEO_" + (String)search_cat.getSelectedItem();
			if (cat.equals("VIDEO_NODE.JS"))
				cat = "video_node_js";
			notice_table.setNumRows(0);
			sql = "select * from project." + cat;
			ResultSet rs = DB_Video.getResult(sql);
			try {
				while(rs.next()) {
					int num = rs.getInt("num");
					String videoname = rs.getString("content");
					String videourl = rs.getString("title");
					Date date = rs.getDate("date");
					int 조회수 = rs.getInt("조회수");
				
					Object data[] = {num,videoname,videourl,date,조회수};
					notice_table.addRow(data);
				}
			} catch (SQLException e1) {
				e1.printStackTrace();
			} finally {
				search_tf.setText("");
			}
		} else if (obj == search_tf || obj == searchBtn) {
			String searchCat = "VIDEO_" + (String)search_cat.getSelectedItem();
			String searchThing = (String)search_com.getSelectedItem();
			String searchText = search_tf.getText();
			String sql = "";
			if(searchText.equals("")) {
				JOptionPane.showMessageDialog(this, "검색어를 한 글자 이상 입력해주세요.", "검색어 오류", JOptionPane.PLAIN_MESSAGE);
				search_tf.setText("");
				return;
			}
			if(searchCat.equals("VIDEO_NODE.JS"))
				searchCat = "video_node_js";
			if(searchThing.equals("Title") || searchThing.equals("Content")) {
				sql = "SELECT * FROM DB." + searchCat + " WHERE " + searchThing + " LIKE '%" + searchText + "%'";
			} else if (searchThing.equals("Num")) {
				try {
					int searchNum = Integer.parseInt(searchText);
					sql = "SELECT * FROM DB." + searchCat + " WHERE " + searchThing + " = " + searchNum;
				} catch (NumberFormatException e2) {
					JOptionPane.showMessageDialog(this, "숫자를 입력해주세요", "검색어 오류", JOptionPane.PLAIN_MESSAGE);
					search_tf.setText("");
					return;
				} finally {
				}
			}
			notice_table.setNumRows(0);
			
			ResultSet rs = DB_Video.getResult(sql);
			try {
				while(rs.next()) {
					int num = rs.getInt("num");
					String videoname = rs.getString("content");
					String videourl = rs.getString("title");
					Date date = rs.getDate("date");
					int 조회수 = rs.getInt("조회수");
				
					Object data[] = {num,videoname,videourl,date,조회수};
					notice_table.addRow(data);
				}
			} catch (SQLException e1) {
				e1.printStackTrace();
			} finally {
				search_tf.setText("");
			}
		} else if(obj == uploadBtn) {
			JFrame VideoManager_Upload = new VideoManager_Upload("VideoManager_Upload");
		} else if(obj == deleteBtn) {
			int input = 1;
			int num = 0;
			int row = main_Board.getSelectedRow();
			TableModel tm = main_Board.getModel();
			try {
				num = (int)tm.getValueAt(row, 0);
			} catch (ArrayIndexOutOfBoundsException e2) {
				JOptionPane.showMessageDialog(this, "동영상을 선택해주세요.", "동영상 미선택", JOptionPane.ERROR_MESSAGE);
			}
			if(num != 0) {
			input = JOptionPane.showConfirmDialog(this, "선택한 동영상은 " + num + "번 동영상입니다.", "동영상 삭제", 
										JOptionPane.YES_NO_CANCEL_OPTION, 
										JOptionPane.CANCEL_OPTION);
			}
			if(input == 0) {
				String sqldel = "";
				String delCat = "VIDEO_" + (String)search_cat.getSelectedItem();
				if(delCat.equals("VIDEO_NODE.JS"))
					delCat = "video_node_js";
				sqldel = "DELETE FROM DB." + delCat + " WHERE NUM=" + num;
				DB_Video.executeSQL(sqldel);
				String sql = "";
				String cat = "VIDEO_" + (String)search_cat.getSelectedItem();
				if (cat.equals("VIDEO_NODE.JS"))
					cat = "video_node_js";
				notice_table.setNumRows(0);
				sql = "select * from DB." + cat;
				ResultSet rs = DB_Video.getResult(sql);
				try {
					while(rs.next()) {
						int num1 = rs.getInt("num");
						String videoname = rs.getString("content");
						String videourl = rs.getString("title");
						Date date = rs.getDate("date");
						int 조회수 = rs.getInt("조회수");
				
						Object data[] = {num1,videoname,videourl,date,조회수};
						notice_table.addRow(data);
					}
				} catch (SQLException e1) {
					e1.printStackTrace();
				} finally {
					search_tf.setText("");
				}
				setVisible(true);
			}
		} else if(obj == refleshBtn) {
			String sql = "";
			String cat = "VIDEO_" + (String)search_cat.getSelectedItem();
			if (cat.equals("VIDEO_NODE.JS"))
				cat = "video_node_js";
			notice_table.setNumRows(0);
			sql = "select * from DB." + cat;
			ResultSet rs = DB_Video.getResult(sql);
			try {
				while(rs.next()) {
					int num = rs.getInt("num");
					String videoname = rs.getString("content");
					String videourl = rs.getString("title");
					Date date = rs.getDate("date");
					int 조회수 = rs.getInt("조회수");
				
					Object data[] = {num,videoname,videourl,date,조회수};
					notice_table.addRow(data);
				}
			} catch (SQLException e1) {
				e1.printStackTrace();
			} finally {
				search_tf.setText("");
			}
			
		}
	}
	@Override
	public void mouseClicked(MouseEvent e) {
		
	}
	@Override
	public void mousePressed(MouseEvent e) {
		
	}
	@Override
	public void mouseReleased(MouseEvent e) {
		
	}
	@Override
	public void mouseEntered(MouseEvent e) {
		
	}
	@Override
	public void mouseExited(MouseEvent e) {
		
	}
}

