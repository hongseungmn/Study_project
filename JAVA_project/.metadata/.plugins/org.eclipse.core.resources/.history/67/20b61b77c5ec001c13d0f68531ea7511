package MainUI;

import java.awt.Color;
import java.awt.Component;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.swing.JTable;
import javax.swing.table.DefaultTableCellRenderer;

import videoUI.DB_Video;

public class VideoTableRender extends DefaultTableCellRenderer {
	
	private String title;
	private DB_Video db = new DB_Video();
	private int total=0;
	private int check_row[] = new int[50];
	private int row;
	private int count = 0;
	
	public VideoTableRender(String title,int userID) {
		this.title = title;
		
		//ResultSet stmt= DB_Video.getResult("SELECT "+ title +",userID FROM DB.CheckVideo WHERE userID = "+userID+" ORDER BY "+title);
//		try {
//			row = 0;
//			while(stmt.next()) {
//				check_row[row] = stmt.getInt(1);
//				row++;
//			}
//		} catch (SQLException e) {
//			e.printStackTrace();
//		}
	};
	@Override
	public Component getTableCellRendererComponent(JTable table, Object value, boolean isSelected, boolean hasFocus, int row, int col) {
		Component c = super.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, col);
		
		if( !table.isRowSelected(row)) {
			
//			if(Integer.parseInt(table.getValueAt(row,0).toString()) == check_row[count]) {
//				c.setBackground(Color.YELLOW);
//				count++;
//			}
			if (row % 2 == 0) {
				c.setBackground(new Color(100,100,100,50));
		    } 
			else {
		    	c.setBackground(new Color(50, 50, 50, 80));
			}
		}
		return c;
	}

}
