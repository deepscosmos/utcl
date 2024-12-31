
import { createRouter, createWebHistory } from "vue-router";
import UTCL from "../views/OPERATIVE_CONSTRAINTS.vue";
import Model from "../views/Model.vue";
import TrendAnalysis from "../views/TrendAnalysis.vue";
import TagMasterDashboard from "../views/TagMasterDashboard.vue";
import OperationalConstraintsDashboard from "../views/OperationalConstraintsDashboard.vue";
import Dashboard from "../views/Dashboard.vue"; // Import the new Dashboard component

const routes = [
  { path: "/", name: "dashboard", component: Dashboard }, // Add Dashboard as the root path
  { path: "/operative_constraint", name: "operative_constraint", component: UTCL },
  { path: "/model", name: "model", component: Model },
  { path: "/trend-analysis", name: "trend-analysis", component: TrendAnalysis },
  { path: "/tag-master", name: "tag-master", component: TagMasterDashboard },
  { 
    path: "/operational-constraints", 
    name: "operational-constraints", 
    component: OperationalConstraintsDashboard 
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

