package MainUI;

import java.awt.Color;

import java.sql.ResultSet;
import java.sql.SQLException;

import org.jfree.chart.ChartPanel;

import org.jfree.chart.JFreeChart;
import org.jfree.chart.axis.CategoryAxis;
import org.jfree.chart.axis.CategoryLabelPositions;
import org.jfree.chart.axis.NumberAxis;
import org.jfree.chart.axis.ValueAxis;
import org.jfree.chart.plot.CategoryPlot;
import org.jfree.chart.plot.DatasetRenderingOrder;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.renderer.category.BarRenderer;
import org.jfree.chart.renderer.category.CategoryItemRenderer;
import org.jfree.chart.renderer.category.LineAndShapeRenderer;
import org.jfree.data.category.DefaultCategoryDataset;
import org.jfree.ui.ApplicationFrame;
import org.jfree.ui.RefineryUtilities;

import videoUI.DB_Video;


public class GraphFrame extends ApplicationFrame {
	public ChartPanel chartPanel;
	private DB_Video useDB = new DB_Video();
	private int userIndex;
	
    public GraphFrame(int userIndex) {

        super("test");
        this.userIndex = userIndex;
        float java_proceed = 0;
        float c_proceed = 0;
        float node_proceed = 0;
        float python_proceed = 0;
        float scratch_proceed = 0;
        float arduino_proceed = 0;
        int total_row = 0;
        useDB.init();
        ResultSet rs1= DB_Video.getResult("SELECT COUNT(DISTINCT java),COUNT(DISTINCT c),COUNT(DISTINCT node_js),COUNT(DISTINCT python),COUNT(DISTINCT scratch),COUNT(DISTINCT arduino) FROM DB.CheckVideo cv WHERE userID = "+ userIndex +" ");
        try {
			while(rs1.next()) {
				java_proceed = rs1.getInt(1);
				c_proceed = rs1.getInt(2);
				node_proceed = rs1.getInt(3);
				python_proceed = rs1.getInt(4);
				scratch_proceed = rs1.getInt(5);
				arduino_proceed = rs1.getInt(6);
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        ResultSet tot= DB_Video.getResult("SELECT COUNT(*) FROM DB.video_java ");
        try {
			while(tot.next()) {
				total_row = tot.getInt(1);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
        
        
        //java_proceed = (java_proceed / total_row)*100;
        

        DefaultCategoryDataset dataset1 = new DefaultCategoryDataset();
        
        dataset1.addValue(java_proceed, "현재 진행 상태", "JAVA");
        dataset1.addValue(c_proceed, "현재 진행 상태", "C");
        dataset1.addValue(node_proceed, "현재 진행 상태", "Node.js");
        dataset1.addValue(python_proceed, "현재 진행 상태", "Python");
        dataset1.addValue(scratch_proceed, "현재 진행 상태", "Scratch");
        dataset1.addValue(arduino_proceed, "현재 진행 상태", "Arduino");
        
        
        
        CategoryItemRenderer renderer = new BarRenderer();
    
        renderer.setDefaultItemLabelsVisible(true);
        
        CategoryPlot plot = new CategoryPlot();
        plot.setDataset(dataset1);
        plot.setRenderer(renderer);
        
        plot.setDomainAxis(new CategoryAxis("수업"));
        plot.setRangeAxis(new NumberAxis("진행률"));

        plot.setOrientation(PlotOrientation.VERTICAL);
        plot.setRangeGridlinesVisible(true);
        plot.setDomainGridlinesVisible(true);
        plot.setBackgroundPaint(Color.WHITE);





        
        plot.setDatasetRenderingOrder(DatasetRenderingOrder.FORWARD);
        
        plot.getDomainAxis().setCategoryLabelPositions(CategoryLabelPositions.STANDARD);
        JFreeChart chart = new JFreeChart(plot);
        chart.setBackgroundPaint(Color.white);
        chart.setTitle("강좌별 수강 진행률");
      

     
        chartPanel = new ChartPanel(chart);
        chartPanel.setPreferredSize(new java.awt.Dimension(450, 330));
        pack();

    }

 
   

}