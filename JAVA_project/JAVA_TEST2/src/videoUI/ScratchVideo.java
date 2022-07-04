package videoUI;

import javax.swing.table.DefaultTableCellRenderer;


import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableCellRenderer;
import javax.swing.table.TableColumnModel;
import javax.swing.text.Document;

import MainUI.MainUI;
import MainUI.TabUI;
import MainUI.VideoTableRender;
import videoUI.DB_Video;

import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.sql.*;


public class ScratchVideo extends JPanel implements MouseListener, ChangeListener, ActionListener{
	
	private JTextField search_tf;
	private JComboBox<String> search_com;
	private DefaultTableModel notice_table;
	private JTable main_Board;
	private int userIndex;
	private String[] url;
	private DefaultTableCellRenderer celTextColor;
	private DefaultTableCellRenderer celTextCenter;
	private DefaultTableCellRenderer celTextLeft;
	private DefaultTableCellRenderer celTextRight;
	private VideoTableRender table_rander;
	private JLabel JavaImageLabel;
	private JPanel JavaPanel;
	private JButton searchBtn;
	private JButton refleshBtn;

	public ScratchVideo(int userIndex) {
	
		setSize(450,660);
		
		setLayout(new BorderLayout());
		setBackground(Color.orange);
		this.userIndex = userIndex;
		
		DB_Video.init();
		
//		데이터베이스 행개수 구하기위해 
		ResultSet rs= DB_Video.getResult("select * from DB.VIDEO_SCRATCH");
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
		ResultSet rs1= DB_Video.getResult("select * from DB.VIDEO_SCRATCH");
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
		
		JPanel video = new JPanel();
		video.setLayout(new BorderLayout());
		
		JPanel search_panel = new JPanel();
		JPanel VIDEO_SCRATCHontent = new JPanel();
		
		String search_list[] = {"Title", "Content", "Num"};
		search_com = new JComboBox<String>(search_list);
		
		search_tf = new JTextField(10);
		search_tf.addActionListener(this);
		
		searchBtn = new JButton("검색");
		searchBtn.addActionListener(this);
		refleshBtn = new JButton("새로고침");
		refleshBtn.addActionListener(this);
		
		search_panel.add(search_com);
		search_panel.add(search_tf);
		search_panel.add(searchBtn);
		search_panel.add(refleshBtn);
		
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
		
		
		main_Board.getTableHeader().setReorderingAllowed(false);
		main_Board.getTableHeader().setResizingAllowed(false);
		main_Board.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
		main_Board.setPreferredScrollableViewportSize(new Dimension(400,470));
		main_Board.setFillsViewportHeight(true);
		table_rander = new VideoTableRender("scratch",userIndex);
		main_Board.setDefaultRenderer(Object.class, table_rander);
		main_Board.addMouseListener(this);
		JScrollPane scrollPane = new JScrollPane(main_Board);
		VIDEO_SCRATCHontent.add(scrollPane);
		
		JavaPanel = new JPanel();
		JavaPanel.setLayout(new BorderLayout());
		
		ImageIcon JavaImage = new ImageIcon("src/img/inclass5.png");
		
		Image image = JavaImage.getImage();
		Image chimg = image.getScaledInstance(450, 150, 200);
		ImageIcon JavaImagech = new ImageIcon(chimg);
		
		JavaImageLabel = new JLabel(JavaImagech);
		
		JPanel ImagePanel = new JPanel();
		ImagePanel.add(JavaImageLabel);
		
		JavaPanel.add(ImagePanel, BorderLayout.CENTER);
		JavaPanel.add(search_panel, BorderLayout.NORTH);
		
		video.add(JavaPanel, BorderLayout.NORTH);
		video.add(VIDEO_SCRATCHontent, BorderLayout.CENTER);
		add(video);
		
		notice_table.setNumRows(0);
		ResultSet rs2= DB_Video.getResult("select * from DB.VIDEO_SCRATCH");


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
			setVisible(true);
		}
	
	@Override
	public void mouseClicked(MouseEvent e) {
		int row = main_Board.getSelectedRow();
		//더블클릭시 url연결
		if (e.getClickCount() == 2) {
		Desktop d = Desktop.getDesktop();
			try {
				d.browse(new URI(url[row]));
			} catch (IOException e1) {
				e1.printStackTrace();
			} catch (URISyntaxException e1) {
				e1.printStackTrace();
			} finally {
		}
			//조회수 증가 
			ResultSet rs= DB_Video.getResult("select 조회수 from DB.VIDEO_SCRATCH where num = " + (row +1));
			try {
				while(rs.next()) {
					int 조회수 = rs.getInt("조회수");
					String updateSQL = "UPDATE DB.VIDEO_SCRATCH SET 조회수=" + 
							(조회수 + 1) + 				
							" WHERE NUM=" + (row+1) + "";
					DB_Video.executeSQL(updateSQL);
				}
			} catch (SQLException e1) {
				e1.printStackTrace();
			}
			ResultSet stmt= DB_Video.getResult("select NUM from DB.VIDEO_SCRATCH where num = " + (row +1));
			try {
				while(stmt.next()) {
					int num = stmt.getInt("NUM");
					String sql = "INSERT INTO DB.CheckVideo(java,c,node_js,python,scratch,userID,arduino) VALUES (NULL ,NULL,NULL,NULL," + num + "," + userIndex + ",NULL )";
					DB_Video.executeSQL(sql);
				}
			} catch (SQLException e1) {
				e1.printStackTrace();
			}
			
		}
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
	@Override
	public void stateChanged(ChangeEvent e) {
		JTabbedPane pane = (JTabbedPane)e.getSource();
		int sel = pane.getSelectedIndex();
	
		if(sel == 1) {
		}
		}
	public DefaultTableModel getTable() {
		return notice_table;
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		Object obj = e.getSource();
		if (obj == refleshBtn) {
			notice_table.setNumRows(0);
			ResultSet rs2= DB_Video.getResult("select * from DB.VIDEO_SCRATCH");
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
				setVisible(true);
				ResultSet rs= DB_Video.getResult("select * from DB.VIDEO_SCRATCH");
				int urltotal = 0;
				try {
					while(rs.next()) {
						urltotal++;
					}
				} catch (SQLException e2) {
					e2.printStackTrace();
				} finally {
					try {
						rs.close();
					} catch (SQLException e2) {
						e2.printStackTrace();
					}
				}
//				url 주소 입력
				url = new String[urltotal];
				ResultSet rs1= DB_Video.getResult("select * from DB.VIDEO_SCRATCH");
				int i = 0;
				try {
					while(rs1.next()) {
						try {
							url[i] = rs1.getString("url");
							i++;
						} catch (SQLException e3) {
							e3.printStackTrace();
						}
					}
				} catch (SQLException e3) {
					e3.printStackTrace();
				} finally {
					try {
						rs1.close();
					} catch (SQLException e3) {
						e3.printStackTrace();
					}
				}
		}
		else if (obj == search_tf || obj == searchBtn) {
			String searchThing = (String)search_com.getSelectedItem();
			String searchText = search_tf.getText();
			String sql = "";
			if(searchText.equals("")) {
				JOptionPane.showMessageDialog(null, "검색어를 한 글자 이상 입력해주세요.", "검색어 오류", JOptionPane.PLAIN_MESSAGE);
				search_tf.setText("");
				return;
			}
			if(searchThing.equals("Title") || searchThing.equals("Content")) {
				sql = "SELECT * FROM DB.VIDEO_SCRATCH WHERE " + searchThing + " LIKE '%" + searchText + "%'";
			} else if (searchThing.equals("Num")) {
				try {
					int searchNum = Integer.parseInt(searchText);
					sql = "SELECT * FROM DB.VIDEO_SCRATCH WHERE " + searchThing + " = " + searchNum;
				} catch (NumberFormatException e2) {
					JOptionPane.showMessageDialog(null, "숫자를 입력해주세요", "검색어 오류", JOptionPane.PLAIN_MESSAGE);
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
			}
		}
		search_tf.setText("");
	}
}
