<template>
  <div class="container">
    <!-- Sidebar with buttons -->
    <div class="sidebar">
      <h1>📊 Trend Lines for Process Data</h1>

      <!-- Fetch Data Button -->
      <button class="primary-button" @click="fetchAndPlotData">Fetch and Plot Data</button>

      <!-- Column Controls -->
      <div v-for="(data, column) in columnsData" :key="column" class="column-controls">
        <h2>{{ column }}</h2>

        <!-- Moving Average Slider -->
        <div class="slider">
          <h3>Moving Average: {{ columnWindows[column] }}</h3>
          <input
            type="range"
            min="1"
            max="50"
            v-model="columnWindows[column]"
            @input="updateMovingAverage(column)"
          />
        </div>

        <!-- Chart Controls -->
        <div class="button-group">
          <button @click="showChart(column, 'timeSeries')">Time Series</button>
          <button @click="showChart(column, 'trend')">Linear Trend</button>
          <button @click="showChart(column, 'movingAverage')">Moving Average</button>
        </div>
      </div>
    </div>

    <!-- Charts Section -->
    <div class="charts">
      <div
        v-for="(data, column) in columnsData"
        :key="column"
        class="chart-container"
      >
        <!-- Time Series Chart -->
        <canvas
          v-show="visibleCharts[column] === 'timeSeries'"
          :id="'chart-' + column"
        ></canvas>

        <!-- Linear Trend Chart -->
        <canvas
          v-show="visibleCharts[column] === 'trend'"
          :id="'chart-trend-' + column"
        ></canvas>

        <!-- Moving Average Chart -->
        <canvas
          v-show="visibleCharts[column] === 'movingAverage'"
          :id="'chart-moving-' + column"
        ></canvas>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, nextTick } from "vue";
import axios from "axios";
import Chart from "chart.js/auto";
import "chartjs-adapter-date-fns";

export default {
  name: "TrendLines",
  setup() {
    const columnsData = ref({});
    const visibleCharts = ref({});
    const columnWindows = ref({});

    const fetchAndPlotData = async () => {
      try {
        const response = await axios.get(
          "http://localhost:8000/process-data-latest"
        );
        const data = response.data;

        const columns = [
          "Kiln_Feed_SP",
          "Kiln_Feed_PV_UL",
          "Kiln_Feed_PV_LL",
          "Calciner_temperature_PV_UL",
        ];
        columns.forEach((column) => {
          columnsData.value[column] = data.map((row) => ({
            TimeStamp: row.TimeStamp,
            value: row[column],
          }));
          columnWindows.value[column] = 15;
        });

        nextTick(() => {
          columns.forEach((column) => {
            createChart(column, columnsData.value[column], "timeSeries");
            createChart(column, columnsData.value[column], "movingAverage");
          });
        });
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    const createChart = (column, data, chartType) => {
      let chartId = "";
      let chartData = [];
      let chartLabel = "";

      if (chartType === "timeSeries") {
        chartId = "chart-" + column;
        chartData = data.map((item) => item.value);
        chartLabel = column + " (Time Series)";
      } else if (chartType === "trend") {
        chartId = "chart-trend-" + column;
        chartData = linearRegression(data.map((item) => item.value));
        chartLabel = column + " (Linear Trend)";
      } else if (chartType === "movingAverage") {
        chartId = "chart-moving-" + column;
        chartData = calculateMovingAverage(
          data.map((item) => item.value),
          columnWindows.value[column]
        );
        chartLabel = column + " (Moving Average)";
      }

      const ctx = document.getElementById(chartId).getContext("2d");
      new Chart(ctx, {
        type: "line",
        data: {
          labels: data.map((item) => item.TimeStamp),
          datasets: [
            {
              label: chartLabel,
              data: chartData,
              borderColor: getColor(chartType),
              tension: 0.1,
              borderWidth: 2,
              fill: false,
              pointRadius: 3,
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              position: "top",
            },
          },
          scales: {
            x: {
              type: "time",
              title: {
                display: true,
                text: "Timestamp",
              },
            },
            y: {
              title: {
                display: true,
                text: "Value",
              },
            },
          },
        },
      });
    };

    const getColor = (chartType) => {
      return {
        timeSeries: "rgba(75, 192, 192, 1)",
        trend: "rgba(255, 99, 132, 1)",
        movingAverage: "rgba(153, 102, 255, 1)",
      }[chartType];
    };

    const linearRegression = (values) => {
      const n = values.length;
      const x = Array.from({ length: n }, (_, i) => i + 1);
      const sumX = x.reduce((a, b) => a + b, 0);
      const sumY = values.reduce((a, b) => a + b, 0);
      const sumXY = x.reduce((acc, xi, i) => acc + xi * values[i], 0);
      const sumX2 = x.reduce((acc, xi) => acc + xi * xi, 0);

      const slope = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
      const intercept = (sumY - slope * sumX) / n;

      return x.map((xi) => slope * xi + intercept);
    };

    const calculateMovingAverage = (data, windowSize) => {
      let movingAvg = [];
      for (let i = 0; i < data.length; i++) {
        const window = data.slice(Math.max(i - windowSize + 1, 0), i + 1);
        const avg = window.reduce((sum, value) => sum + value, 0) / window.length;
        movingAvg.push(avg);
      }
      return movingAvg;
    };

    const updateMovingAverage = (column) => {
      const data = columnsData.value[column];
      createChart(column, data, "movingAverage");
    };

    const showChart = (column, chartType) => {
      visibleCharts.value[column] = chartType;
      createChart(column, columnsData.value[column], chartType);
    };

    return {
      columnsData,
      visibleCharts,
      fetchAndPlotData,
      showChart,
      columnWindows,
      updateMovingAverage,
    };
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-wrap: wrap;
  background-color: #f9f9f9;
  font-family: Arial, sans-serif;
}

.sidebar {
  flex: 1;
  padding: 20px;
  background: #fff;
  border-right: 1px solid #ddd;
}

.primary-button {
  background: #007bff;
  color: #fff;
  padding: 10px;
  margin-bottom: 15px;
  border: none;
  cursor: pointer;
  transition: background 0.3s ease;
}

.primary-button:hover {
  background: #0056b3;
}

.column-controls {
  margin: 15px 0;
}

.button-group button {
  margin: 5px;
  background: #28a745;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  border-radius: 3px;
  transition: background 0.3s ease;
}

.button-group button:hover {
  background: #218838;
}

.charts {
  flex: 3;
  padding: 20px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 15px;
}

.chart-container {
  position: relative;
  background: #fff;
  border-radius: 8px;
  border: 1px solid #ddd;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  height: 300px;
  padding: 10px;
}

.chart-container canvas {
  width: 100%;
  height: 100%;
}

.slider {
  margin: 10px 0;
}
</style>
