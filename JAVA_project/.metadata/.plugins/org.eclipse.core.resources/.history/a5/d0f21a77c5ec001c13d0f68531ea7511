package MainUI;

import javax.swing.JTable;

import java.awt.*;
import javax.swing.*;
import javax.swing.table.DefaultTableCellRenderer;

public class TableRender extends DefaultTableCellRenderer {
	int row_num=0;
	@Override
	public Component getTableCellRendererComponent(JTable table, Object value, boolean isSelected, boolean hasFocus, int row, int col) {
		Component c = super.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, col);
		if( !table.isRowSelected(row)) {
			
			if(table.getValueAt(row,4).toString().equals("YES")) {
				c.setBackground(Color.YELLOW);
			}
			
			else {
				c.setBackground(new Color(200,200,200,50));
			}
			
		}
		row_num++;
		return c;
	}

}
