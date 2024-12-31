<template>
  <div>
    <h2>Dashboard</h2>
    <div class="chart-container">
      <!-- Bar chart -->
      <!-- <Bar :chart-data="chartData" :chart-options="chartOptions" /> -->
    </div>
  </div>
</template>
    
    <script setup>
import { ref, onMounted } from "vue";
import { Bar } from "vue-chartjs";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

// Fetch data from FastAPI backend
onMounted(async () => {
  try {
    const response = await fetch("http://127.0.0.1:8000/status-counts"); // FastAPI endpoint
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    console.log("Success:", data.success);
    console.log("Failure:", data.failure);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
});

const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    title: {
      display: true,
      text: "Success vs Failure",
      font: {
        size: 18,
      },
    },
    legend: {
      position: "top",
    },
  },
  scales: {
    y: {
      beginAtZero: true,
    },
  },
});
</script>
    
    <style scoped>
.chart-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  height: 400px; /* Ensure the chart has enough space */
}

canvas {
  max-width: 100%;
  height: 100%;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
  font-size: 1.8em;
}
</style>
    