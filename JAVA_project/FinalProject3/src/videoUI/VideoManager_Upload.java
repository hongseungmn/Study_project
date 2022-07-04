package videoUI;

import java.awt.BorderLayout;

import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.SQLIntegrityConstraintViolationException;
import java.sql.SQLSyntaxErrorException;
import java.util.Vector;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;



public class VideoManager_Upload extends JFrame implements ActionListener{
	
	
	private Vector<String> vecCombo;
	private JComboBox<String> combo;
	private JTextField tf;
	private JTextField upDatetf;
	private JButton uploadBtn;
	private JButton cancleBtn;
	private JTextField UrlTf;
	private JTextField Filtertf;
	private Vector<String> vecFilter;
	private JComboBox<String> Filtercombo;
	private String selectedItem;

	public VideoManager_Upload(String title) {
		setTitle(title);
		setSize(300, 320);
		setLayout(null);
		setLocationRelativeTo(null);
		setResizable(false);
		
		JLabel content_video = new JLabel("Content");
		content_video.setFont(new Font("Gothic",Font.BOLD , 12));
		content_video.setBounds(40, 10, 50, 20);
		add(content_video);
		
		vecCombo = new Vector<String>();
		vecCombo.add("카테고리");
		vecCombo.add("자바");
		vecCombo.add("C");
		vecCombo.add("node_js");
		vecCombo.add("파이썬");
		vecCombo.add("스크래치");
		vecCombo.add("아두이노");
		
		combo = new JComboBox<String>(vecCombo);
		combo.setBounds(40, 30, 80, 30);
		combo.addActionListener(this);
		add(combo);
		
		vecFilter = new Vector<String>();
		
		
		Filtercombo = new JComboBox<String>(vecFilter);
		Filtercombo.setBounds(130, 30, 110, 30);
		Filtercombo.enable(false);
		add(Filtercombo);
		
//		Filtertf = new JTextField(20);
//		Filtertf.setBounds(150, 30, 90, 30);
//		add(Filtertf);
		
		JLabel contentFilter = new JLabel("Filter");
		contentFilter.setBounds(130, 10, 50, 20);
		add(contentFilter);
		
		JLabel title_video = new JLabel("Title");
		title_video.setBounds(40, 65, 50, 10);
		add(title_video);
		
		tf = new JTextField(20);
		tf.setBounds(40, 80, 200, 30);
		
		add(tf);
		
		JLabel upload_date = new JLabel("Upload Date");
		upload_date.setBounds(40, 115, 100, 15);
		add(upload_date);
		
		upDatetf = new JTextField(20);
		upDatetf.setBounds(40, 135, 200, 30);
		upDatetf.setText("1999.01.01");
		
		add(upDatetf);
		
		uploadBtn = new JButton("올리기");
		cancleBtn = new JButton("취소");
		
		uploadBtn.addActionListener(this);
		uploadBtn.setBounds(50, 235, 80, 30);
		add(uploadBtn);
		cancleBtn.addActionListener(this);
		cancleBtn.setBounds(140, 235, 80, 30);
		add(cancleBtn);
		
		JLabel videoUrl = new JLabel("Video URL");
		videoUrl.setBounds(40, 170, 100, 15);
		add(videoUrl);
		
		UrlTf = new JTextField(20);
		UrlTf.setBounds(40, 190, 200, 30);
		add(UrlTf);
		
		
		
		setVisible(true);
		vecCombo.remove("카테고리");
		
	}
		


	public static void main(String[] args) {
		VideoManager_Upload tf = new VideoManager_Upload("동영상 올리기");
	}


	@Override
	public void actionPerformed(ActionEvent e) {
		Object obj = e.getSource();
		if(obj == uploadBtn) {
			DB_Video.init();
			int num = 1;
			String categori = "";
			String content = (String)combo.getSelectedItem();
			if (content.equals("자바")) {
				categori = "video_java";
			} else if (content.equals("C")) {
				categori = "video_c";
			} else if (content.equals("node_js")) {
				categori = "video_node_js";
			} else if (content.equals("파이썬")) {
				categori = "video_python";
			} else if (content.equals("스크래치")) {
				categori = "VIDEO_SCRATCH";
			} else if (content.equals("아두이노")) {
				categori = "video_arduino";
			}
			content = (String)Filtercombo.getSelectedItem();
			String title = tf.getText();
			String date = upDatetf.getText();
			String url = UrlTf.getText();
			String sql = ("SELECT NUM FROM DB." + categori);
			if(title.equals("") || url.equals("") || title.equals(null) || url.equals(null) || content.equals(null) || categori.equals("카테고리")) {
				JOptionPane.showConfirmDialog(this, "입력정보를 확인하세요.", "업로드 오류", JOptionPane.PLAIN_MESSAGE, JOptionPane.ERROR_MESSAGE);
				return;
			} 
			ResultSet rs = DB_Video.getResult(sql);
			int i = 1;
			try {
				while(rs.next()) {
					num = rs.getInt("num");
					if(i < num) {
						num = i;
						break;
					}
					num += 1;
					i++;
				}
			} catch (SQLException e1) {
				
			} 
			finally {
				try {
					rs.close();
				} catch (SQLException e1) {
					e1.printStackTrace();
				} catch (NullPointerException e1) {
					JOptionPane.showConfirmDialog(this, "입력정보를 확인하세요.", "업로드 오류", JOptionPane.PLAIN_MESSAGE, JOptionPane.ERROR_MESSAGE);
					return;
				}
			} 
			int input;
			input = JOptionPane.showConfirmDialog(this, "동영상 번호 : " + num + "\n" +
														"동영상 분류 : " + content + "\n" +
														"동영상 제목 : " + title + "\n" +
														"동영상 게시일자 : " + date + "\n" +
														"동영상 url : " + url + "\n"
					,"동영상 업로드", 
					JOptionPane.YES_NO_OPTION, 
					JOptionPane.QUESTION_MESSAGE);
			if (input == 0) {
//			String sqlin = ("INSERT INTO PROJECT." + categori + " (NUM, CONTENT, TITLE, 'date' , 조회수, URL)VALUES(" + (num) + ""
//					+ ", '" + content + "', '" + title + "" + "', '" + date + "', 0, '" + url + "')");
			String sqlin = ("INSERT INTO DB."  + categori + " (NUM, CONTENT, TITLE, `date`, 조회수, URL) VALUES(" + num + ", '" + content + "', '"  + title + "',"
					+ " '"  + date + "', 0, '"  + url + "')");
			DB_Video.executeSQL(sqlin);
			tf.setText("");
			upDatetf.setText("");
			UrlTf.setText("");
			}
		} else if (obj == combo) {
			Filtercombo.setSelectedItem(null);
			selectedItem = (String)combo.getSelectedItem();
			if(selectedItem.equals("자바") && !vecFilter.contains("자바 기초")) {
				Filtercombo.enable(true);
				vecFilter.clear();
				vecFilter.add("자바 기초");
				vecFilter.add("자바 응용");
			} else if(selectedItem.equals("C") && !vecFilter.contains("C언어 기초")) {
				Filtercombo.enable(true);
				vecFilter.clear();
				vecFilter.add("C언어 기초");
				vecFilter.add("C언어 기초");
			} else if(selectedItem.equals("node_js") && !vecFilter.contains("node.js서버개발")) {
				Filtercombo.enable(true);
				vecFilter.clear();
				vecFilter.add("node.js서버개발");
			} else if(selectedItem.equals("파이썬") && !vecFilter.contains("파이썬 기초")) {
				Filtercombo.enable(true);
				vecFilter.clear();
				vecFilter.add("파이썬 기초");
			} else if(selectedItem.equals("스크래치") && !vecFilter.contains("스크래치 3.0")) {
				Filtercombo.enable(true);
				vecFilter.clear();
				vecFilter.add("스크래치 3.0");
			} else if(selectedItem.equals("아두이노") && !vecFilter.contains("아두이노 기초")) {
				Filtercombo.enable(true);
				vecFilter.clear();
				vecFilter.add("아두이노 기초");
			} 
		} else if (obj == cancleBtn) {
			if(JOptionPane.showConfirmDialog(this,
					"입력된 정보는 사라집니다. 종료하시겠습니까?",
					"종료",
					JOptionPane.YES_NO_OPTION,
					JOptionPane.ERROR_MESSAGE
					) == JOptionPane.YES_OPTION) {
			setVisible(false);
			}
		}
	}
}
