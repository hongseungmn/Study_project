package MainUI;

import javax.swing.*;  
import java.awt.HeadlessException;  
import java.awt.BorderLayout;  
import java.awt.FlowLayout;  
import java.awt.Font;  
import java.awt.event.ActionListener;  
import java.awt.event.ActionEvent;  

public class StopWatch extends JFrame implements ActionListener {  

	private static String time_label = "00:00:00";   
    private CountingThread thread = new CountingThread();            
    private long programStart = System.currentTimeMillis();          
    private long pauseStart = programStart;           
    private long pauseCount = 0;     
    private JLabel label = new JLabel(time_label);    
    private JButton startPauseButton = new JButton("시작");    
    private JButton resetButton = new JButton("초기화");   
    
    public StopWatch(String title) {  
        super(title);  
        setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);   
        setResizable(false);  
        setLocationRelativeTo(getParent());
        setSize(250,150);
        setupBorder();  
        setupLabel();  
        setupButtonsPanel();  
   
        startPauseButton.addActionListener(this);  
        resetButton.addActionListener(this);  
   
        thread.start();              
    }  
   
    private void setupBorder() {  
        JPanel contentPane = new JPanel(new BorderLayout());  
        contentPane.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));  
        this.setContentPane(contentPane);  
    }  
   
    //       
    private void setupButtonsPanel() {  
        JPanel panel = new JPanel(new FlowLayout());  
        panel.add(startPauseButton);  
        panel.add(resetButton);  
        add(panel, BorderLayout.SOUTH);  
    }  
   
    //       
    private void setupLabel() {  
        label.setHorizontalAlignment(SwingConstants.CENTER);  
        label.setFont(new Font(label.getFont().getName(), label.getFont().getStyle(), 40));  
        this.add(label, BorderLayout.CENTER);  
    }  
    private class CountingThread extends Thread {  
    	   
        public boolean stopped = true;  
   
        private CountingThread() {  
            setDaemon(true);  
        }  
   
        @Override  
        public void run() {  
            while (true) {  
                if (!stopped) {  
                    long elapsed = System.currentTimeMillis() - programStart - pauseCount;  
                    label.setText(format(elapsed));  
                }  
   
                try {  
                    sleep(1);  // 1        
                } catch (InterruptedException e) {  
                    e.printStackTrace();  
                    System.exit(1);  
                }  
            }  
        }  
   
        //          
        private String format(long elapsed) {  
            int hour, minute, second, milli;  
   
           
            elapsed = elapsed / 1000;  
   
            second = (int) (elapsed % 60);  
            elapsed = elapsed / 60;  
   
            minute = (int) (elapsed % 60);  
            elapsed = elapsed / 60;  
   
            hour = (int) (elapsed % 60);  
   
            return String.format("%02d:%02d:%02d", hour, minute, second);  
        }  
    }
	@Override
	public void actionPerformed(ActionEvent e) {
		Object obj = e.getSource();
		if(obj == startPauseButton) {
			if (thread.stopped) {  
                pauseCount += (System.currentTimeMillis() - pauseStart);  
                thread.stopped = false;  
                startPauseButton.setText("정지 ");  
            } else {  
                pauseStart = System.currentTimeMillis();  
                thread.stopped = true;  
                startPauseButton.setText("재시작");  
            } 
		}
		else if (obj == resetButton) {
			pauseStart = programStart;  
            pauseCount = 0;  
            thread.stopped = true;  
            label.setText(time_label);  
            startPauseButton.setText("초기화");  
		}
		
	}  
}  
