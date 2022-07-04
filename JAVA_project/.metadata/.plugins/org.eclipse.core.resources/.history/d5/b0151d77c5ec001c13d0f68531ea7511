package MainUI;




import javax.swing.table.DefaultTableCellRenderer;






import videoUI.JavaVideo;
import videoUI.ArduinoVideo;
import videoUI.C_Video;
import videoUI.Node_jsVideo;
import videoUI.PythonVideo;
import videoUI.ScratchVideo;
import videoUI.*;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableColumnModel;
import javax.swing.text.Document;

import MainUI.MainUI.ImagePanel;

import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.sql.*;







public class MainUI extends JFrame implements ActionListener, ChangeListener, MouseListener, WindowListener {
	
	private RoundButton write_board;
	private JTabbedPane TP;
	private JButton search_btn;
	private JComboBox<String> search_com;
	private JTextField search_tf;
	private JButton link_btn;
	private JButton changeGraphBtn;
	private ImageIcon class1_Icon;
	private ImageIcon class1_Intro;
	private ImageIcon class2_Icon;
	private ImageIcon class2_Intro;
	private ImageIcon class3_Icon;
	private ImageIcon class3_Intro;
	private ImageIcon class4_Icon;
	private ImageIcon class4_Intro;
	private ImageIcon class5_Icon;
	private ImageIcon class5_Intro;
	private ImageIcon class6_Icon;
	private ImageIcon class6_Intro;
	private JLabel class1_label;
	private JLabel class2_label;
	private JLabel class3_label;
	private JLabel class4_label;
	private JLabel class5_label;
	private JLabel class6_label;
	private JPanel addGraph;
	private JButton add_button;
	private JTextField set_hour;
	private JTextField set_minutes;
	private JButton class1_btn;
	private JButton class2_btn;
	private JButton class3_btn;
	private JButton class4_btn;
	private JButton class5_btn;
	private JButton class6_btn;
	private Image tab2_resizeImage;
	public ClientFrame clientFrame;
	public String userId;
	private int userIndex;
	protected JTable main_Board;
	public DB_Mysql useDB = new DB_Mysql(); 
	public DefaultTableModel notice_table;
	public JPanel graphPanel;
	public JPanel graphPanel2;
	public JavaVideo javaVideo;
	public ArduinoVideo arduinoVideo;
	public Node_jsVideo node_jsVideo;
	public VideoPanel videoPanel;
	
	
	public MainUI(String userId,int userIndex) {
		setTitle("MainUI");
		setSize(1000,1000);
		setLocationRelativeTo(this);
		setLayout(new BorderLayout());
		setResizable(false);
		setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
		this.userId = userId;
		this.userIndex = userIndex;
		addWindowListener(this);
		TP = new JTabbedPane();
		UIManager.put("TabbedPane.selected", new Color(255,255,255));
		TP.setBackground(new Color(136,141,200));
		TP.setUI(new TabUI());
		
		JPanel mainBack = new JPanel();
		ImageIcon main_background= new ImageIcon("src/img/mainback.png");
		Image main_backImage = main_background.getImage();
		int mainWidth = main_backImage.getWidth(null);
		int mainHeight = main_backImage.getHeight(null);
			
		int Width = 1000;
			
		double rt = (double)Width/(double)mainWidth;
			
		int wt = (int)(mainWidth * rt);
		int ht = (int)(mainHeight * rt);
			
		Image resizeMainImage = main_backImage.getScaledInstance(wt, ht, Image.SCALE_SMOOTH);
		JLabel mainImage = new JLabel(new ImageIcon(resizeMainImage));
		add(mainImage,BorderLayout.NORTH);
		
		
		
		// 메인 가운데 이미지
//		
		
		  
		// tab1 
		JPanel tab1 = new JPanel();
		tab1.setLayout(null);
		ImageIcon background= new ImageIcon("src/img/mainback3.png");
		Image backImage = background.getImage();
		int srcWidth = backImage.getWidth(null);
		int srcHeight = backImage.getHeight(null);
			
		int newWidth = 1000;
			
		double ratio = (double)newWidth/(double)srcWidth;
			
		int w = (int)(srcWidth * ratio);
		int h = (int)(srcHeight * ratio);
			
		Image resizeImage = backImage.getScaledInstance(w, h, Image.SCALE_SMOOTH);
		JLabel main_main = new JLabel(new ImageIcon(resizeImage));
		
		
		
		ImageIcon link_icon = new ImageIcon("src/img/Button1.png");
		Image link_image = link_icon.getImage();
		link_image = link_image.getScaledInstance(30, 30, Image.SCALE_SMOOTH);
		link_icon = new ImageIcon(link_image);
		link_btn = new JButton("자세하게 알아보기 =>(Click!!)",link_icon);
		link_btn.setFont(new Font("고딕",Font.BOLD,15));
		link_btn.addActionListener(this);
		
		tab1.add(link_btn);
		link_btn.setBounds(750,5,250,40);
		tab1.add(main_main);
		main_main.setBounds(0,0,1000,700);
		
		//tab2
		
		ImageIcon MainImage = new ImageIcon("src/img/back2.jpg");
		
		Image image = MainImage.getImage();
		Image chimg = image.getScaledInstance(980, 1000, 200);
		ImageIcon MainImagech = new ImageIcon(chimg);
		
		ImagePanel tab2 = new ImagePanel(MainImagech.getImage());
		
		JPanel search_panel = new JPanel();
		search_panel.setBounds(0, 0, tab2.getWidth(), 50);
		
		JPanel main_content = new JPanel();
		main_content.setBounds(130, 50, 720,640);
		main_content.setBorder(BorderFactory.createLineBorder(Color.black,5));
		
		ImageIcon tab2_background= new ImageIcon("src/img/mainback3.png");
		Image tab2_backImage = background.getImage();
		int tab2_srcWidth = backImage.getWidth(null);
		int tab2_srcHeight = backImage.getHeight(null);
		
		tab2.setLayout(null);
		
		
			
		int tab2_newWidth = 1000;
			
		double tab2_ratio = (double)tab2_newWidth/(double)tab2_srcWidth;
			
		int tab2_w = (int)(tab2_srcWidth * tab2_ratio);
		int tab2_h = (int)(tab2_srcHeight * tab2_ratio);
			
		tab2_resizeImage = tab2_backImage.getScaledInstance(tab2_w, tab2_h, Image.SCALE_SMOOTH);
		JLabel tab2_main_main = new JLabel(new ImageIcon(tab2_resizeImage));
		
		
		String search_list[] = {"id","content","title","date"};
		search_com = new JComboBox<String>(search_list);
		
		search_tf = new JTextField(20);
		ImageIcon img = new ImageIcon("src/img/search_Icon.png");
		Image changeImage = img.getImage();
		changeImage = changeImage.getScaledInstance(20, 20, Image.SCALE_SMOOTH);
		img = new ImageIcon(changeImage);
		search_btn = new JButton("search..",img);
		search_btn.setBorderPainted(false); 
		search_btn.setFocusPainted(false); 
		search_btn.setContentAreaFilled(false);
		search_btn.addActionListener(this);
		
		
		write_board = new RoundButton("글쓰기");
		write_board.setBounds(20, 5, 20, 50);
		write_board.addActionListener(this);
		
	
		
		search_panel.setBackground(new Color(136,141,200));
		search_panel.add(search_com);
		search_panel.add(search_tf);
		search_panel.add(search_btn);
		search_panel.add(write_board);
		tab2.add(search_panel,BorderLayout.NORTH);
		
		
		String header[] = new String[] {"ID","Title","ConTents","Date","Answer"};

		
		notice_table = new DefaultTableModel(header,0) {
			public boolean isCellEditable(int i, int c) {
				return false;
			} 
		};
		
		
		
		main_Board = new JTable(notice_table);	
		main_Board.setRowHeight(25);
		main_Board.getColumn("ID").setPreferredWidth(2);
		main_Board.getColumn("Title").setPreferredWidth(50);
		main_Board.getColumn("ConTents").setPreferredWidth(200);
		main_Board.getColumn("Date").setPreferredWidth(10);
		main_Board.getColumn("Answer").setPreferredWidth(2);
		TableRender table_rander = new TableRender();
		
		main_Board.getTableHeader().setReorderingAllowed(false);
		main_Board.getTableHeader().setResizingAllowed(false);
		main_Board.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
		main_Board.setPreferredScrollableViewportSize(new Dimension(700,600));
		main_Board.setFillsViewportHeight(true);
		main_Board.setDefaultRenderer(Object.class, table_rander);
		main_Board.addMouseListener(new MouseListener() {

			@Override
			public void mouseClicked(MouseEvent e) {
				if(e.getClickCount() == 2) {
					int row = main_Board.getSelectedRow();
					System.out.println(main_Board.getValueAt(row,2));
					String contents = (String) main_Board.getValueAt(row, 2);
					useDB.selectDB("SELECT answer_Content FROM DB.TB where Content ='" + contents + "'");
					String answer ="";
					try {
						if(useDB.rs.next()) {
							answer = useDB.rs.getString("answer_Content");
						}
						
					} catch (SQLException e1) {
						// TODO Auto-generated catch block
						e1.printStackTrace();
					}
					System.out.println(answer);
					new Content(contents,answer);
				}
			}

			@Override
			public void mousePressed(MouseEvent e) {
				// TODO Auto-generated method stub
				
			}

			@Override
			public void mouseReleased(MouseEvent e) {
				// TODO Auto-generated method stub
				
			}

			@Override
			public void mouseEntered(MouseEvent e) {
				// TODO Auto-generated method stub
				
			}

			@Override
			public void mouseExited(MouseEvent e) {
				// TODO Auto-generated method stub
				
			}
			
		});
		JScrollPane scrollPane = new JScrollPane(main_Board);
		main_content.add(scrollPane);
		
		
		
		
		tab2.add(main_content,BorderLayout.CENTER);
		
//		tab2_main_main.setBounds(0,0,1000,700);
//		tab2.add(tab2_main_main);
		
		
		//tab3
		ImageIcon tabp3_back = new ImageIcon("src/img/back2.jpg");
		
		Image tabp3_image = tabp3_back.getImage();
		Image tabp3_chimage = tabp3_image.getScaledInstance(980, 1000, 200);
		ImageIcon tabp3_backch = new ImageIcon(tabp3_chimage);
		
		ImagePanel tab3 = new ImagePanel(tabp3_backch.getImage());
		tab3.setLayout(null);
		
		JPanel class_panel = new JPanel();
		class_panel.setLayout(new FlowLayout(FlowLayout.LEFT,30,20));
		Dimension size = new Dimension();
		size.setSize(1500,300);
		class_panel.setPreferredSize(size);
		
		
		JScrollPane class_scroll = new JScrollPane();
		class_scroll.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_NEVER);
		class_scroll.setViewportView(class_panel);
		
		
		JPanel class_1 = new JPanel();
		class_1.setBackground(new Color(189,186,222));
		class_1.setLayout(new BoxLayout(class_1,BoxLayout.Y_AXIS));
		Dimension class_size = new Dimension();
		class_size.setSize(200,350);
		class_1.setPreferredSize(class_size);
		
		class1_Icon = new ImageIcon("src/img/class_1.png");
		Image class1_Image = class1_Icon.getImage();
		class1_Image = class1_Image.getScaledInstance(200, 200, Image.SCALE_SMOOTH);
		class1_Icon = new ImageIcon(class1_Image);
		class1_label = new JLabel(class1_Icon);
		
		class1_Intro = new ImageIcon("src/img/class1_intro.png");
		Image class1_ItroImg = class1_Intro.getImage();
		class1_ItroImg = class1_ItroImg.getScaledInstance(200, 200, Image.SCALE_SMOOTH);
		class1_Intro = new ImageIcon(class1_ItroImg);
		
		
		class1_label.addMouseListener(this);
		class_1.add(class1_label);
		
		class1_btn = new JButton("Java 수업들으러 가기");
		class1_btn.setPreferredSize(new Dimension(200,100));
		class_1.add(class1_btn);
		class1_btn.addActionListener(this);
		
		
		JPanel class_2 = new JPanel();
		class_2.setBackground(new Color(189,186,222));
		class_2.setLayout(new BoxLayout(class_2,BoxLayout.Y_AXIS));
		class_2.setPreferredSize(class_size);
		
		class2_Icon = new ImageIcon("src/img/class_2.png");
		Image class2_Image = class2_Icon.getImage();
		class2_Image = class2_Image.getScaledInstance(200,200,Image.SCALE_SMOOTH);
		class2_Icon = new ImageIcon(class2_Image);
		class2_label = new JLabel(class2_Icon);
		class2_label.addMouseListener(this);
		class2_btn = new JButton("C 수업들으러 가기");
		class2_btn.setPreferredSize(new Dimension(200,100));
		class2_btn.addActionListener(this);
		class2_Intro = new ImageIcon("src/img/class2_intro.png");
		Image class2_ItroImg = class2_Intro.getImage();
		class2_ItroImg = class2_ItroImg.getScaledInstance(200, 200, Image.SCALE_SMOOTH);
		class2_Intro = new ImageIcon(class2_ItroImg);
		
		class_2.add(class2_label);
		class_2.add(class2_btn);
		
		
		
		
		JPanel class_3 = new JPanel();
		class_3.setBackground(new Color(189,186,222));
		class_3.setLayout(new BoxLayout(class_3,BoxLayout.Y_AXIS));
		class_3.setPreferredSize(class_size);
		
		class3_Icon = new ImageIcon("src/img/class_3.png");
		Image class3_Image = class3_Icon.getImage();
		class3_Image = class3_Image.getScaledInstance(200,200,Image.SCALE_SMOOTH);
		class3_Icon = new ImageIcon(class3_Image);
		class3_label = new JLabel(class3_Icon);
		class3_Intro = new ImageIcon("src/img/class3_intro.png");
		Image class3_ItroImg = class3_Intro.getImage();
		class3_ItroImg = class3_ItroImg.getScaledInstance(200, 200, Image.SCALE_SMOOTH);
		class3_Intro = new ImageIcon(class3_ItroImg);
		class_3.add(class3_label);
		class3_label.addMouseListener(this);
		class3_btn = new JButton("Node.js 수업들으러 가기");
		class3_btn.setPreferredSize(new Dimension(200,100));
		class_3.add(class3_btn);
		class3_btn.addActionListener(this);
		
		
		
		JPanel class_4 = new JPanel();
		class_4.setBackground(new Color(189,186,222));
		class_4.setLayout(new BoxLayout(class_4,BoxLayout.Y_AXIS));
		class_4.setPreferredSize(class_size);
		
		class4_Icon = new ImageIcon("src/img/class_4.png");
		Image class4_Image = class4_Icon.getImage();
		class4_Image = class4_Image.getScaledInstance(200,200,Image.SCALE_SMOOTH);
		class4_Icon = new ImageIcon(class4_Image);
		class4_label = new JLabel(class4_Icon);
		class4_Intro = new ImageIcon("src/img/class4_intro.png");
		Image class4_ItroImg = class4_Intro.getImage();
		class4_ItroImg = class4_ItroImg.getScaledInstance(200, 200, Image.SCALE_SMOOTH);
		class4_Intro = new ImageIcon(class4_ItroImg);
		class_4.add(class4_label);
		class4_label.addMouseListener(this);
		class4_btn = new JButton("Python 수업들으러 가기");
		class4_btn.setPreferredSize(new Dimension(200,100));
		class_4.add(class4_btn);
		class4_btn.addActionListener(this);
		
		JPanel class_5 = new JPanel();
		class_5.setBackground(new Color(189,186,222));
		class_5.setLayout(new BoxLayout(class_5,BoxLayout.Y_AXIS));
		class_5.setPreferredSize(class_size);
		
		class5_Icon = new ImageIcon("src/img/class_5.png");
		Image class5_Image = class5_Icon.getImage();
		class5_Image = class5_Image.getScaledInstance(200,200,Image.SCALE_SMOOTH);
		class5_Icon = new ImageIcon(class5_Image);
		class5_label = new JLabel(class5_Icon);
		class5_Intro = new ImageIcon("src/img/class5_intro.png");
		Image class5_ItroImg = class5_Intro.getImage();
		class5_ItroImg = class5_ItroImg.getScaledInstance(200, 200, Image.SCALE_SMOOTH);
		class5_Intro = new ImageIcon(class5_ItroImg);
		class_5.add(class5_label);
		class5_label.addMouseListener(this);
		class5_btn = new JButton("Scratch 수업들으러 가기");
		class5_btn.setPreferredSize(new Dimension(200,100));
		class_5.add(class5_btn);
		class5_btn.addActionListener(this);
		
		JPanel class_6 = new JPanel();
		class_6.setBackground(new Color(189,186,222));
		class_6.setLayout(new BoxLayout(class_6,BoxLayout.Y_AXIS));
		class_6.setPreferredSize(class_size);
		
		class6_Icon = new ImageIcon("src/img/class_6.png");
		Image class6_Image = class6_Icon.getImage();
		class6_Image = class6_Image.getScaledInstance(200,200,Image.SCALE_SMOOTH);
		class6_Icon = new ImageIcon(class6_Image);
		class6_label = new JLabel(class6_Icon);
		class6_Intro = new ImageIcon("src/img/class6_intro.png");
		Image class6_ItroImg = class6_Intro.getImage();
		class6_ItroImg = class6_ItroImg.getScaledInstance(200, 200, Image.SCALE_SMOOTH);
		class6_Intro = new ImageIcon(class6_ItroImg);
		class_6.add(class6_label);
		class6_label.addMouseListener(this);
		class6_btn = new JButton("Arduino 수업들으러 가기");
		class6_btn.setPreferredSize(new Dimension(200,100));
		class_6.add(class6_btn);
		class6_btn.addActionListener(this);
		
		
		
		
		class_panel.add(class_1);
		class_panel.add(class_2);
		class_panel.add(class_3);
		class_panel.add(class_4);
		class_panel.add(class_5);
		class_panel.add(class_6);
		class_panel.setBackground(new Color(189,186,222));
		
		
		graphPanel = new JPanel();
		GraphFrame graph = new GraphFrame(userIndex);
		graphPanel.add(graph.chartPanel);
		
		graphPanel2 = new JPanel();
		GraphFrame2 graph2 = new GraphFrame2("Graph",userIndex);
		graphPanel2.add(graph2.chartPanel);
		
		changeGraphBtn = new JButton("공부시간 확인하기");
		changeGraphBtn.addActionListener(this);
		
		
		addGraph = new JPanel();
		addGraph.setLayout(new FlowLayout());
		JLabel timeAdd = new JLabel("공부시간 추가");
		set_hour = new JTextField(2);
		JLabel sep = new JLabel(":");
		set_minutes = new JTextField(2);
		add_button = new JButton("추가");
		add_button.addActionListener(this);
		
		
		
		addGraph.add(timeAdd);
		addGraph.add(set_hour);
		addGraph.add(sep);
		addGraph.add(set_minutes);
		addGraph.add(add_button);
		addGraph.setBackground(new Color(136,141,200, 0));
		
		
		
		
		
		
		JPanel chatPanel = new JPanel();
		
		clientFrame = new ClientFrame("Client");
		chatPanel.add(clientFrame);
		
		
		
		
		
		tab3.add(class_scroll);
		class_scroll.setBorder(BorderFactory.createLineBorder(Color.black,5));
		tab3.add(graphPanel);
		tab3.add(graphPanel2);
		tab3.add(changeGraphBtn);
		tab3.add(addGraph);
		tab3.add(chatPanel);
		JLabel chatTitle = new JLabel("실시간 공지사항");
		chatTitle.setFont(new Font("맑은고딕",Font.BOLD,20));
		tab3.add(chatTitle);
		
		//tab3.add(video);
		tab3.setBackground(new Color(136,141,200));
		
		
		
		class_scroll.setBounds(5,5,980,300);
		graphPanel.setBounds(5,350,480,350);
		graphPanel.setBorder(BorderFactory.createLineBorder(Color.black,5));
		graphPanel2.setBounds(5,350,480,350);
		graphPanel2.setBorder(BorderFactory.createLineBorder(Color.black,5));
		chatPanel.setBounds(500,350,480,350);
		chatPanel.setBorder(BorderFactory.createLineBorder(Color.black,5));
		changeGraphBtn.setBounds(5,320,150,30);
		addGraph.setBounds(200,315,250,50);
		addGraph.setVisible(false);
		chatTitle.setBounds(670,315,200,50);

			
																															
																		
																								
																							
		
		//tab1 이미지
		ImageIcon tab1_image = new ImageIcon("src/img/tab1Image.png");
		Image tab1_imageChange = tab1_image.getImage();
		tab1_imageChange = tab1_imageChange.getScaledInstance(20, 20, Image.SCALE_SMOOTH);
		tab1_image = new ImageIcon(tab1_imageChange);
		
		
		
		//tab2 이미지
		ImageIcon tab2_image = new ImageIcon("src/img/tab2Image.png");
		Image tab2_imageChange = tab2_image.getImage();
		tab2_imageChange = tab2_imageChange.getScaledInstance(20, 20, Image.SCALE_SMOOTH);
		tab2_image = new ImageIcon(tab2_imageChange);
		
		
		
		//tab3 이미지
		ImageIcon tab3_image = new ImageIcon("src/img/tab3Image.png");
		Image tab3_imageChange = tab3_image.getImage();
		tab3_imageChange = tab3_imageChange.getScaledInstance(20, 20, Image.SCALE_SMOOTH);
		tab3_image = new ImageIcon(tab3_imageChange);
		
		
		
		TP.addTab("Show",tab1_image,tab3);
		TP.addTab("게시판",tab2_image,tab2);
		TP.addTab("도움말",tab3_image,tab1);
		TP.addChangeListener(this);
		add(TP,BorderLayout.CENTER);
		
		setVisible(true);

		videoPanel = new VideoPanel(userIndex);
		videoPanel.setVisible(false);
		useDB.connectDB();
		StopWatch timer = new StopWatch("공부시간 측정");
		timer.setVisible(true);
		
		Thread th = new Thread((Runnable) clientFrame);
		th.start();
		
	}
	




	@Override
	public void actionPerformed(ActionEvent e) {
		Object obj = e.getSource();
		if(obj == write_board) {
			new Notice_board(this);
		}
		else if ((obj == search_btn) && (search_com.getSelectedItem() !=null)) {
			String find_range = search_com.getSelectedItem().toString();
			notice_table.setNumRows(0); //테이블 초기화 후 추가
			String find_keyword = search_tf.getText();
			
			useDB.keyword_selectDB("SELECT * FROM DB.TB WHERE "+ find_range +" LIKE '%"+find_keyword+"%'");
			try {
				System.out.println("Query OK");
				while(useDB.rs.next()) {
					String id = useDB.rs.getString("id");
					String title = useDB.rs.getString("title");
					String content = useDB.rs.getString("content");
					Date date = useDB.rs.getDate("date");
					String answer = useDB.rs.getString("answer");
					Object data[] = {id,title,content,date,answer};
					notice_table.addRow(data);
					
				}
			} catch (SQLException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			
		}
		else if (obj == link_btn) {
			if (Desktop.isDesktopSupported()) {
	            Desktop desktop = Desktop.getDesktop();
	            try {
	                URI uri = new URI("https://namu.wiki/w/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8");
	                desktop.browse(uri);
	            } catch (IOException ex) {
	                ex.printStackTrace();
	            } catch (URISyntaxException ex) {
	                ex.printStackTrace();
	            }
			}
		}
		else if (obj == changeGraphBtn) {
			String flag = changeGraphBtn.getText();
			if(flag.equals("공부시간 확인하기"))
			{
				graphPanel.setVisible(false);
				graphPanel2.setVisible(true);
				addGraph.setVisible(true);
				changeGraphBtn.setText("수업별 수강률 확인하기");
			}
			else if(flag.equals("수업별 수강률 확인하기"))
			{
				graphPanel.setVisible(true);
				graphPanel2.setVisible(false);
				addGraph.setVisible(false);
				changeGraphBtn.setText("공부시간 확인하기");
			}
		}
		else if (obj == add_button) {
				String hour = set_hour.getText();
				String minute = set_minutes.getText();
				int thour = Integer.parseInt(hour);
				int tminute = Integer.parseInt(minute);
				int total = (thour*60) + tminute;
				
				useDB.selectDB("SELECT Date,id FROM DB.StudyTime WHERE Date = CURDATE() AND id=" + userIndex + " ");
				try {
					if(useDB.rs.next()) {
						JOptionPane.showMessageDialog(this, "이미 공부시간을 삽입하였습니다","ERROR",JOptionPane.ERROR_MESSAGE);
					}
					else {
						System.out.println("공부한 시간 : " + total + "분을 추가하겠습니다.");
						useDB.graphInsertDB(userIndex,total);
						JOptionPane.showMessageDialog(this, "공부한 시간 : " + total + "분을 추가하겠습니다.","ConFirm",JOptionPane.PLAIN_MESSAGE);
						
					}
				} catch (SQLException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				
				
				
				set_hour.setText("");
				set_minutes.setText("");
		}
		else if( obj == class1_btn) {
			videoPanel.setVisible(true);
			videoPanel.setPanel(1);
		}
		else if(obj == class2_btn) {
			videoPanel.setVisible(true);
			videoPanel.setPanel(2);
		}
		else if(obj == class3_btn) {
			videoPanel.setVisible(true);
			videoPanel.setPanel(3);
		}
		else if(obj == class4_btn) {
			videoPanel.setVisible(true);
			videoPanel.setPanel(4);
		}
		else if(obj == class5_btn) {
			videoPanel.setVisible(true);
			videoPanel.setPanel(5);
		}
		else if(obj == class6_btn) {
			videoPanel.setVisible(true);
			videoPanel.setPanel(6);
		}
		
	}
	
	
	@Override
	public void stateChanged(ChangeEvent e) {
		JTabbedPane pane = (JTabbedPane)e.getSource();
		int sel = pane.getSelectedIndex();
		System.out.println(sel); //0,1,2
		if(sel == 1) {
			notice_table.setNumRows(0);
			useDB.selectDB("SELECT * FROM DB.TB");
			try {
				
				while(useDB.rs.next()) {
					String id = useDB.rs.getString("id");
					String title = useDB.rs.getString("title");
					String content = useDB.rs.getString("content");
					Date date = useDB.rs.getDate("date");
					String answer = useDB.rs.getString("answer");
					Object data[] = {id,title,content,date,answer};
					notice_table.addRow(data);
				}
			} catch (SQLException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			
		}
		
		
		
	}
	@Override
	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void mouseEntered(MouseEvent e) {
		JLabel la = (JLabel)e.getSource();
		if(la == class1_label) 
		{
			la.setIcon(class1_Intro);
		}
		else if(la == class2_label) 
		{
			la.setIcon(class2_Intro);
		}
		else if(la == class3_label) 
		{
			la.setIcon(class3_Intro);
		}
		else if(la == class4_label) 
		{
			la.setIcon(class4_Intro);
		}
		else if(la == class5_label) 
		{
			la.setIcon(class5_Intro);
		}
		else if(la == class6_label) 
		{
			la.setIcon(class6_Intro);
		}
		
		
		
	}
	@Override
	public void mouseExited(MouseEvent e) {
		JLabel la = (JLabel)e.getSource();
		if(la == class1_label) 
		{
			la.setIcon(class1_Icon);
		}
		else if(la == class2_label)
		{
			la.setIcon(class2_Icon);
		}
		else if(la == class3_label)
		{
			la.setIcon(class3_Icon);
		}
		else if(la == class4_label)
		{
			la.setIcon(class4_Icon);
		}
		else if(la == class5_label)
		{
			la.setIcon(class5_Icon);
		}
		else if(la == class6_label)
		{
			la.setIcon(class6_Icon);
		}
		
		
	}
	
	
	public DefaultTableModel getTable() {
		return notice_table;
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
	
//	class MyJPanel extends JFrame {
//		 public void paintComponent(Graphics g){
//	            super.paintComponents(g);
//	            g.drawImage(tab2_resizeImage,0,0,getWidth(),getHeight(),this);
//	        }
//	
//	}

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


