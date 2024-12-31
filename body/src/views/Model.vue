<template>
  <div>
    <h2>Model Performance Dashboard</h2>

    <!-- Buttons for each model -->
    <div class="button-container">
      <button
        v-for="model in models"
        :key="model.name"
        @click="showModelChart(model.name)"
        class="model-button"
      >
        {{ model.name }}
      </button>
    </div>

    <!-- Chart for the selected model -->
    <div v-if="selectedModel" class="chart-container">
      <h3>{{ selectedModel.name }}</h3>
      <Line :data="selectedModel.chartData" :options="chartOptions" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

// Register Chart.js components
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

// Reactive references
const models = ref([]);
const selectedModel = ref(null);

const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { position: "top" },
  },
  scales: {
    y: { beginAtZero: true },
  },
});

// Fetch data
const fetchModelData = async () => {
  try {
    const response = await fetch("http://127.0.0.1:8000/models");
    if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
    const data = await response.json();

    // Group data by ModelName
    const groupedData = data.reduce((acc, item) => {
      if (!acc[item.ModelName]) acc[item.ModelName] = [];
      acc[item.ModelName].push(item);
      return acc;
    }, {});

    // Prepare chart data for each model
    models.value = Object.keys(groupedData).map((modelName) => {
      const modelData = groupedData[modelName];
      const metrics = ["test_mae", "test_mae_dummy", "test_mae_ann"];
      const datasets = metrics.map((metric, index) => ({
        label: metric,
        data: modelData.map((entry) => entry[metric]),
        borderColor: ["blue", "red", "green"][index],
        borderWidth: 2,
        fill: false,
      }));

      return {
        name: modelName,
        chartData: {
          labels: modelData.map((_, index) => index + 1),
          datasets,
        },
      };
    });
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

const showModelChart = (modelName) => {
  selectedModel.value = models.value.find((model) => model.name === modelName);
};

onMounted(fetchModelData);
</script>

<style scoped>
.button-container {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 20px;
}

.model-button {
  margin: 5px;
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1em;
  transition: background-color 0.3s;
}

.model-button:hover {
  background-color: #0056b3;
}

.chart-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  height: 400px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #f9f9f9;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
  font-size: 2em;
}

h3 {
  text-align: center;
  margin-bottom: 10px;
  font-size: 1.5em;
}
</style>
