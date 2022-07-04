package videoUI;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import javax.swing.JOptionPane;

public class DB_Video {

	public static Connection conn;
	public static Statement stmt;

	public static void init() {
			try {
				Class.forName("com.mysql.cj.jdbc.Driver");
				
				conn = DriverManager.getConnection(
						"jdbc:mysql://localhost:3306/DB?allowPublicKeyRetrieval=true&useSSL=false", 
						"connectuser", 
						"connect123!@#");
				
				stmt = conn.createStatement();
			} catch (ClassNotFoundException e) {
				System.out.println("예외 발생 : 해당 드라이버가 없습니다.");
				e.printStackTrace();
			} catch (SQLException e) {
				System.out.println("예외 발생 : 접속 정보 확인이 필요합니다.");
				e.printStackTrace();
			}
	}
	
	// 조회용
	public static ResultSet getResult(String sql) {
		try {
			Statement stmt = conn.createStatement();
			return stmt.executeQuery(sql);
		} catch (SQLException e) {
			e.printStackTrace();
			return null;
		}
	}
	
	// 수정용
	public static void executeSQL(String sql) {
		try {
			stmt.executeUpdate(sql);
		} catch (SQLException e) {
			e.printStackTrace();
			return;
		}
	}
}
