import unittest
import time_series_visualizer
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for testing

class DataVisualizerTests(unittest.TestCase):
    def test_line_plot(self):
        fig = time_series_visualizer.draw_line_plot()
        self.assertEqual(fig.axes[0].get_title(), "Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
        self.assertEqual(fig.axes[0].get_xlabel(), "Date")
        self.assertEqual(fig.axes[0].get_ylabel(), "Page Views")

    def test_bar_plot(self):
        fig = time_series_visualizer.draw_bar_plot()
        self.assertEqual(fig.axes[0].get_xlabel(), "Years")
        self.assertEqual(fig.axes[0].get_ylabel(), "Average Page Views")
        labels = [label.get_text() for label in fig.axes[0].get_legend().get_texts()]
        self.assertIn("January", labels)
        self.assertIn("December", labels)

    def test_box_plot(self):
        fig = time_series_visualizer.draw_box_plot()
        self.assertEqual(fig.axes[0].get_title(), "Year-wise Box Plot (Trend)")
        self.assertEqual(fig.axes[1].get_title(), "Month-wise Box Plot (Seasonality)")
        self.assertEqual(fig.axes[0].get_xlabel(), "Year")
        self.assertEqual(fig.axes[0].get_ylabel(), "Page Views")
        self.assertEqual(fig.axes[1].get_xlabel(), "Month")
        self.assertEqual(fig.axes[1].get_ylabel(), "Page Views")

if __name__ == "__main__":
    unittest.main()
