package MainUI;

import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;

import javax.swing.plaf.basic.BasicTabbedPaneUI;

public class TabUI extends BasicTabbedPaneUI{

	protected void paintTabBorder(Graphics g, int tabPlacement, int tabIndex, int x, int y, int w, int h, boolean isSelected) {
		// TODO Auto-generated method stub
		//보통 보이는 부분 여기서 그려주고
		g.setColor(new Color(136,141,200));
		g.drawRoundRect(x, y, w, h, 10, 10);
		if (isSelected)
		{
			//여기는 선택시 보여주는 부분을 그려주면 됩니다.   
			Graphics2D g2 = (Graphics2D) g;
			g2.setStroke(new BasicStroke(5));
			g2.drawLine(x+4 , y+4 ,  x+w-4 , y+4);
		}
 	}
	
}
