package MainUI;


import java.awt.Color;
import java.sql.SQLException;
import java.text.SimpleDateFormat;
import java.util.Calendar;

import javax.swing.JPanel;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.axis.DateAxis;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYItemRenderer;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.data.category.DefaultCategoryDataset;
import org.jfree.data.time.Day;
import org.jfree.data.time.Month;
import org.jfree.data.time.TimeSeries;
import org.jfree.data.time.TimeSeriesCollection;
import org.jfree.data.xy.XYDataset;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;
import org.jfree.ui.ApplicationFrame;
import org.jfree.ui.RectangleInsets;
import org.jfree.ui.RefineryUtilities;
 
 
public class GraphUser extends ApplicationFrame{
	public ChartPanel chartPanel;
	private DB_Mysql useDB = new DB_Mysql();
	private String namelist[] = new String[100];
	
	public GraphUser(String title) {
		super(title);
		useDB.connectDB();
		 XYDataset dataset = createDataset();
	        JFreeChart chart = createChart(dataset);
	        chartPanel = new ChartPanel(chart, false);
	        chartPanel.setPreferredSize(new java.awt.Dimension(700, 700));
	        chartPanel.setMouseZoomable(true, false);
	        setContentPane(chartPanel);
	        
	        
	        this.pack();

	}

	private JFreeChart createChart(XYDataset dataset) {
		JFreeChart chart = ChartFactory.createTimeSeriesChart(
	            "My Study Schedules",  // title
	            "Date",             // x-axis label
	            "Study Minutes",   // y-axis label
	            dataset,            
	            true,               
	            true,               
	            false              
	        );

	        chart.setBackgroundPaint(Color.white);

	        XYPlot plot = (XYPlot) chart.getPlot();
	        plot.setBackgroundPaint(Color.WHITE);
	        plot.setDomainGridlinePaint(Color.white);
	        plot.setRangeGridlinePaint(Color.white);
	        
	        plot.setDomainCrosshairVisible(true);
	        plot.setRangeCrosshairVisible(true);
	        
	        XYItemRenderer r = plot.getRenderer();
	        if (r instanceof XYLineAndShapeRenderer) {
	            XYLineAndShapeRenderer renderer = (XYLineAndShapeRenderer) r;
	            renderer.setDefaultShapesVisible(true);
	            renderer.setDefaultShapesFilled(true);
	            
	        }
	        
	        DateAxis axis = (DateAxis) plot.getDomainAxis();
	        axis.setDateFormatOverride(new SimpleDateFormat("yy-MM-dd"));
	        
	        return chart;
		
	}

	private XYDataset createDataset() {
		
		TimeSeriesCollection dataset = new TimeSeriesCollection();
		String sql = "SELECT COUNT(*) FROM DB.USER";
		int count =0;
		
		
		useDB.selectDB(sql);
		try {
			if(useDB.rs.next()) {
				count = useDB.rs.getInt(1);
			}
			
		} catch (SQLException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		System.out.println(count);
		
		
		
		
	
		TimeSeries series[] = new TimeSeries[count];
		
		String com = "SELECT userName FROM DB.USER u ORDER BY u.INDEX ASC ";
		
		
		
		for(int i=1;i<=count;i++) {
			//String command = "SELECT time, Date,u.UserName FROM DB.StudyTime st,DB.`USER` u  WHERE st.id = u.`index` AND st.id = "+ i +"";
			useDB.selectDB(com);
			try {
				int j=0;
				while(useDB.rs.next()) {
					namelist[j] = useDB.rs.getString(1);
					System.out.println(namelist[j]);
					j++;
				}
			} catch (SQLException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			
			
			String command = "SELECT time, Date FROM DB.StudyTime WHERE id = " + i + "";
			
			useDB.selectDB(command);
			series[i-1] = new TimeSeries(namelist[i-1]);
			
			try {
				while(useDB.rs.next()) {
					
					int time = useDB.rs.getInt(1);
					System.out.println(time);
					Calendar date = Calendar.getInstance();
					date.setTime(useDB.rs.getDate("Date"));
					
					int day = date.get(Calendar.DATE);
					int month = date.get(Calendar.MONTH);
					int year = date.get(Calendar.YEAR);
					
					
					
					series[i-1].add(new Day(day,month+1,year),time);
					
					
				}
				
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			dataset.addSeries(series[i-1]);
		}
		
	
		
		return dataset;
	}  
    

  
}
