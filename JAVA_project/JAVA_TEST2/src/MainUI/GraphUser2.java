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


public class GraphUser2 extends ApplicationFrame {
	public ChartPanel chartPanel;
	private DB_Video useDB = new DB_Video();
	private String userName;
	
    public GraphUser2(String title,Color color) {

        super("test");
        float java_proceed = 0;
        int total_row = 0;
        useDB.init();
        DefaultCategoryDataset dataset1 = new DefaultCategoryDataset();
        //ResultSet rs1= DB_Video.getResult("SELECT userID ,COUNT(DISTINCT "+ title +") FROM DB.CheckVideo GROUP BY userID;");
        ResultSet rs1 = DB_Video.getResult("SELECT userName ,COUNT(DISTINCT "+ title +") FROM DB.CheckVideo ck, DB.USER u   WHERE ck.userID = u.index GROUP BY u.userName ");
        try {
			while(rs1.next()) {
				userName = rs1.getString(1);
				java_proceed = rs1.getInt(2);
				dataset1.addValue(java_proceed, "현재 진행 상태", ""+userName);
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        
        

        
        
        
        CategoryItemRenderer renderer = new BarRenderer();
    
        renderer.setDefaultItemLabelsVisible(true);
       
   
        
        CategoryPlot plot = new CategoryPlot();
        plot.setDataset(dataset1);
        plot.setRenderer(renderer);
        plot.getRenderer().setSeriesPaint(0,color);
        
        
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
        chart.setTitle(title);
      

     
        chartPanel = new ChartPanel(chart);
        chartPanel.setPreferredSize(new java.awt.Dimension(730, 280));
        pack();

    }

 
   

}