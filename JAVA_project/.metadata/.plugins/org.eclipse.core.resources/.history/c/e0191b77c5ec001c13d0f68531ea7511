package MainUI;

import java.awt.BorderLayout;

import java.awt.Color;

import javax.swing.JFrame;
import javax.swing.JPanel;

import videoUI.C_Video;
import videoUI.JavaVideo;
import videoUI.Node_jsVideo;
import videoUI.PythonVideo;
import videoUI.ScratchVideo;
import videoUI.ArduinoVideo;

public class VideoPanel extends JFrame {
	private int userIndex;
	private C_Video cVideo;
	private JavaVideo javaVideo;
	private Node_jsVideo nodejsVideo;
	private PythonVideo pythonVideo;
	private ScratchVideo scratchVideo;
	private ArduinoVideo arduinoVideo;
	public VideoPanel(int userIndex) {
		setTitle("Video");
		this.userIndex = userIndex;
		setResizable(false);
		setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE);
		setSize(450,700);
		setLocation(1200,100);
		setLayout(new BorderLayout());
		setBackground(Color.orange);
		
		javaVideo = new JavaVideo(userIndex);
		this.add(javaVideo,BorderLayout.CENTER);
		javaVideo.setVisible(true);
		
		cVideo = new C_Video(userIndex);
		this.add(cVideo,BorderLayout.CENTER);
		cVideo.setVisible(false);
		
		nodejsVideo = new Node_jsVideo(userIndex);
		this.add(nodejsVideo,BorderLayout.CENTER);
		nodejsVideo.setVisible(false);
		
		pythonVideo = new PythonVideo(userIndex);
		this.add(pythonVideo,BorderLayout.CENTER);
		pythonVideo.setVisible(false);
		
		scratchVideo = new ScratchVideo(userIndex);
		this.add(scratchVideo,BorderLayout.CENTER);
		scratchVideo.setVisible(false);
		
		arduinoVideo = new ArduinoVideo(userIndex);
		this.add(arduinoVideo,BorderLayout.CENTER);
		arduinoVideo.setVisible(false);
		
		setVisible(true);
		
	}
	
	public void setPanel(int select) {
		if(select == 1) {
			javaVideo.setVisible(true);
			cVideo.setVisible(false);
			nodejsVideo.setVisible(false);
			pythonVideo.setVisible(false);
			scratchVideo.setVisible(false);
			arduinoVideo.setVisible(false);
			
		}
		else if(select == 2) {
			
			javaVideo.setVisible(false);
			cVideo.setVisible(true);
			nodejsVideo.setVisible(false);
			pythonVideo.setVisible(false);
			scratchVideo.setVisible(false);
			arduinoVideo.setVisible(false);
		
		}
		else if(select == 3) {
			javaVideo.setVisible(false);
			cVideo.setVisible(false);
			nodejsVideo.setVisible(true);
			pythonVideo.setVisible(false);
			scratchVideo.setVisible(false);
			arduinoVideo.setVisible(false);
		}
		else if(select == 4) {
			javaVideo.setVisible(false);
			cVideo.setVisible(false);
			nodejsVideo.setVisible(false);
			pythonVideo.setVisible(true);
			scratchVideo.setVisible(false);
			arduinoVideo.setVisible(false);
		}
		else if(select == 5) {
			javaVideo.setVisible(false);
			cVideo.setVisible(false);
			nodejsVideo.setVisible(false);
			pythonVideo.setVisible(false);
			scratchVideo.setVisible(true);
			arduinoVideo.setVisible(false);
		}
		else if(select == 6) {
			javaVideo.setVisible(false);
			cVideo.setVisible(false);
			nodejsVideo.setVisible(false);
			pythonVideo.setVisible(false);
			scratchVideo.setVisible(false);
			arduinoVideo.setVisible(true);
		}
		
		
	}
	
}
