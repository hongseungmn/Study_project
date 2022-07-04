package MainUI;

import java.awt.Color;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.RenderingHints;

import javax.swing.Action;
import javax.swing.Icon;
import javax.swing.JButton;

public class RoundButton extends JButton {
	public RoundButton() { super(); decorate(); } 
    public RoundButton(String text) { super(text); decorate(); } 
    public RoundButton(Action action) { super(action); decorate(); } 
    public RoundButton(Icon icon) { super(icon); decorate(); } 
    public RoundButton(String text, Icon icon) { super(text, icon); decorate(); } 
    protected void decorate() { setBorderPainted(false); setOpaque(false); }
    @Override 
    protected void paintComponent(Graphics g) {
    	
       Color c=new Color(255,255,255); //배경색 결정
       Color o=new Color(0,0,0); //글자색 결정
       
       int width = getWidth(); 
       int height = getHeight(); 
       
       Graphics2D graphics = (Graphics2D) g; 
       graphics.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON); 
       
       if (getModel().isArmed()) { graphics.setColor(c.darker()); } 
       else if (getModel().isRollover()) { graphics.setColor(c.brighter()); } 
       else { graphics.setColor(c); } 
       
       graphics.fillRoundRect(0, 0, width, height, 10, 10); 
       FontMetrics fontMetrics = graphics.getFontMetrics(); 
       Rectangle stringBounds = fontMetrics.getStringBounds(this.getText(), graphics).getBounds(); 
       
       int textX = (width - stringBounds.width) / 2; 
       int textY = (height - stringBounds.height) / 2 + fontMetrics.getAscent(); 
       
       
       graphics.setColor(o); 
       graphics.setFont(new Font("맑은고딕",Font.ITALIC,15)); 
       graphics.drawString(getText(), textX, textY); 
       graphics.dispose(); 
       
       super.paintComponent(g); 
       }

}
