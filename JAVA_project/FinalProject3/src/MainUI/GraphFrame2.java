package MainUI;

import java.awt.Color;
import java.sql.Date;
import java.sql.SQLException;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Calendar;

import javax.swing.JPanel;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.axis.DateAxis;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYItemRenderer;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.data.time.Day;
import org.jfree.data.time.Month;
import org.jfree.data.time.TimeSeries;
import org.jfree.data.time.TimeSeriesCollection;
import org.jfree.data.xy.XYDataset;
import org.jfree.ui.ApplicationFrame;
import org.jfree.ui.RectangleInsets;
import org.jfree.ui.RefineryUtilities;


public class GraphFrame2 extends ApplicationFrame {
	public ChartPanel chartPanel;
	private DB_Mysql useDB = new DB_Mysql();
	private int userIndex;

    public GraphFrame2(String title,int userIndex) {
    	
        super(title);
        useDB.connectDB();
        this.userIndex = userIndex;
        XYDataset dataset = createDataset();
        JFreeChart chart = createChart(dataset);
        chartPanel = new ChartPanel(chart, false);
        chartPanel.setPreferredSize(new java.awt.Dimension(450, 330));
        chartPanel.setMouseZoomable(true, false);
        setContentPane(chartPanel);
        
        this.pack();
    }

    
    private static JFreeChart createChart(XYDataset dataset) {

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

        TimeSeries s1 = new TimeSeries("Minutes");
        
        useDB.graphSelectDB(userIndex);
        try {
			while(useDB.rs.next()) {
				int time = useDB.rs.getInt("time");
				Calendar date = Calendar.getInstance();
				date.setTime(useDB.rs.getDate("Date"));
				System.out.println(date);
				int day = date.get(Calendar.DATE);
				System.out.println("day"+day);
				int month = date.get(Calendar.MONTH);
				System.out.println("month"+month);
				int year = date.get(Calendar.YEAR);
				System.out.println(year);
				s1.add(new Day(day,month+1,year),time);
				
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
        
        

     

        TimeSeriesCollection dataset = new TimeSeriesCollection();
        dataset.addSeries(s1);
        

        return dataset;

    }
    
   
}