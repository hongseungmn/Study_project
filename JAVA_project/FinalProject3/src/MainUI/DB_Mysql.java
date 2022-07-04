package MainUI;

import java.sql.*;



import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class DB_Mysql {
	private String URL ="jdbc:mysql://localhost:3306/DB?allowPublicKeyRetrieval=true&useSSL=false";
	private String ID = "connectuser";
	private String PW = "connect123!@#";
	public java.sql.PreparedStatement stmt;
	public java.sql.PreparedStatement stmt2;
	public java.sql.PreparedStatement stmt3;
	public java.sql.PreparedStatement stmt4;
	public java.sql.PreparedStatement stmt5;
	public java.sql.PreparedStatement stmt6;
	public java.sql.PreparedStatement stmt7;
	public java.sql.PreparedStatement stmt8;
	public java.sql.PreparedStatement stmt9;
	public Connection conn;
	public java.sql.ResultSet rs;
	
	
	
	public void connectDB() {
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
			System.out.println("Driver 로딩 성공");
			conn = DriverManager.getConnection(URL,ID,PW);
			System.out.println("OK");
			
		
		} catch (ClassNotFoundException e) {
			System.out.println("예외 발생 : 해당 드라이버가 없습니다" );
			e.printStackTrace();
			
		} catch (SQLException e) {
			System.out.println("서버 연결 실패");
			e.printStackTrace();
		}
	}
		
	public void insertDB(String id, String title, String content,String date) {
		try {
				
			String sql = " INSERT INTO DB.TB(id,title,content,date,answer) " + " VALUES('" + id + "','" + title + "','" + content + "','" + date + "','"+ "NO" +"') ";
			stmt = conn.prepareStatement(sql);
			this.stmt.executeUpdate(sql);
			System.out.println("added ok");
		} catch (Exception e){
			System.out.println("InsertError" + e);
		}
	}
	
	
	public void selectDB(String command) {
		try {
			stmt2 = conn.prepareStatement(command);
			this.rs = this.stmt2.executeQuery(command);
			
		} catch (SQLException e) {
			System.out.println("selectError" + e);
		}
	}
	
	public void keyword_selectDB(String command) {
		try {
			stmt3 = conn.prepareStatement(command);
			System.out.println(stmt3);
	
			this.rs = this.stmt3.executeQuery(command);
			
		} catch (SQLException e) {
			System.out.println("selectError" + e);
		}
	}
	
	public void login_selectDB(String command) {
		try {
			stmt5 = conn.prepareStatement(command);
			System.out.println(stmt5);
			this.rs = this.stmt5.executeQuery(command);
			
		} catch (SQLException e) {
			System.out.println("selectError" + e);
		}
	}
	
	public void updateDB(String contents) {
			
			try {
				String sql = " UPDATE DB.TB SET answer = 'YES' WHERE Content = '"+ contents +"'";
				stmt4 = conn.prepareStatement(sql);
				System.out.println(sql);
				this.stmt4.executeUpdate(sql);
				System.out.println("Update OK");
			} catch (SQLException e) {
				System.out.println("UpdateError" + e);
			}
		}
	
	public void closeDB() {
		try {
			conn.close();
		} catch (SQLException e) {
			System.out.println("closeError" + e);
		}
	}
	
	public void graphInsertDB(int userIndex, int time) {
		try {
			String sql = " INSERT INTO DB.StudyTime(id,time,date) " + " VALUES( " + userIndex + ",'" + time + "',now()) ";
			System.out.println(sql);
		
			stmt6 = conn.prepareStatement(sql);
			this.stmt6.executeUpdate(sql);
			System.out.println("added ok");
		} catch (Exception e){
			System.out.println("InsertError" + e);
		}
	}
	
	public void graphSelectDB(int userIndex) {
		try {
			String sql = "SELECT * FROM DB.StudyTime where id = " + userIndex + "";
			System.out.println(sql);
			stmt7 = conn.prepareStatement(sql);
			this.rs = this.stmt7.executeQuery(sql);
			System.out.println("Query OK");
		} catch (SQLException e) {
		
			e.printStackTrace();
		}
	}
	
	public void updateAnswer(String content,String answer) {
		try {
			String sql = " UPDATE DB.TB SET answer_Content = '" + answer + "' WHERE Content = '"+ content +"'";
			stmt4 = conn.prepareStatement(sql);
			System.out.println(sql);
			this.stmt4.executeUpdate(sql);
			System.out.println("Update OK");
		} catch (SQLException e) {
			System.out.println("UpdateError" + e);
		}
	}
	
	public void deleteBoard(String title,String content) {
		String sql = "DELETE FROM DB.TB WHERE title = '" + title + "' AND Content = '" + content + "'";
		try {
			stmt8 = conn.prepareStatement(sql);
			System.out.println(sql);
			this.stmt8.executeUpdate();
		} catch (SQLException e) {

			e.printStackTrace();
		}
	}
	
	public void insertUser(String id, String pw, String email) {
		
		try {
			String sql = "INSERT INTO DB.USER " + " VALUES('" + pw + "','" + email + "', NULL ,'" + id + "') ";
			System.out.println(sql);
			stmt9 = conn.prepareStatement(sql);
			this.stmt9.executeUpdate(sql);
			System.out.println("added ok");
		} catch (SQLException e) {
		
			e.printStackTrace();
		}
	}
	
	public void deleteUser(int index) {
		String sql = "DELETE FROM DB.`USER` WHERE `index` = '" + index + "'";
		try {
			stmt8 = conn.prepareStatement(sql);
			System.out.println(sql);
			this.stmt8.executeUpdate();
		} catch (SQLException e) {

			e.printStackTrace();
		}
	}
	
	

}
