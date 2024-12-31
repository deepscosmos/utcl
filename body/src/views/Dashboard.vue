<template>
  <div class="dashboard-container">
    <h1>Dashboard</h1>
    <div class="routes-grid">
      <!-- Loop through all the routes and display them as cards -->
      <div 
        class="route-card" 
        v-for="route in routes" 
        :key="route.path" 
        @click="navigate(route.path)"
      >
        <div class="icon-container">
          <i class="route-icon fas fa-route"></i>
        </div>
        <h2>{{ route.name }}</h2>
        <p>Explore {{ route.name }} features.</p>
      </div>
    </div>
  </div>
</template>

<script>
import { useRouter } from "vue-router";

export default {
  name: "Dashboard",
  setup() {
    const router = useRouter();

    // Filter routes to exclude the dashboard route itself
    let routes = router.options.routes.filter(route => route.name !== "dashboard");

    // Sort routes to prioritize "Tag Master" first, then "Operational Constraints", followed by others
    routes.sort((a, b) => {
      const priorityOrder = ["Tag Master", "Operational Constraints"];
      const aIndex = priorityOrder.indexOf(a.name);
      const bIndex = priorityOrder.indexOf(b.name);

      if (aIndex === -1 && bIndex === -1) {
        // If neither is in the priority list, maintain default order
        return 0;
      }
      if (aIndex === -1) {
        // If 'a' is not in the priority list, it comes after 'b'
        return 1;
      }
      if (bIndex === -1) {
        // If 'b' is not in the priority list, it comes after 'a'
        return -1;
      }
      // If both are in the priority list, sort by their index in the list
      return aIndex - bIndex;
    });

    const navigate = (path) => {
      router.push(path);
    };

    return { routes, navigate };
  },
};
</script>

<style scoped>
/* Overall container styling */
.dashboard-container {
  text-align: center;
  padding: 20px;
  background-color: #f8f9fa;
  min-height: 100vh;
}

/* Header styling */
h1 {
  font-size: 2.5rem;
  margin-bottom: 30px;
  color: #343a40;
}

/* Grid layout for cards */
.routes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  justify-items: center;
  align-items: center;
  padding: 20px;
}

/* Individual card styling */
.route-card {
  background-color: #ffffff;
  border: 1px solid #dee2e6;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 20px;
  text-align: center;
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  width: 100%;
  max-width: 300px;
}

.route-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
}

/* Icon container styling */
.icon-container {
  background-color: #007bff;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 auto 15px;
}

.route-icon {
  color: #ffffff;
  font-size: 1.5rem;
}

/* Text styling */
h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
  color: #343a40;
}

p {
  font-size: 1rem;
  color: #6c757d;
}
</style>
