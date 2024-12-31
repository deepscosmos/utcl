<template>
  <div>
    <h1>Operational Constraints Dashboard</h1>
    <DataTable
      :title="'Operational Constraints'"
      :data="tableData"
      :columns="columns"
      @add="handleAdd"
      @delete="handleDelete"
      @save="handleSave"
    />
  </div>
</template>

<script>
import DataTable from "../../component/DataTable.vue";

export default {
  name: "OperationalConstraintsDashboard",
  components: { DataTable },
  data() {
    return {
      tableData: [
        {
          entry_var: "Clinker_temperature",
          entry_limit_type: "UL",
          neighbour_var: "Mid_tap_temperature",
          neighbour_limit_type: "LL",
          step_size: 0.05,
          total_shift: 0.15,
        },
        {
          entry_var: "Clinker_temperature",
          entry_limit_type: "UL",
          neighbour_var: "Secondary_Air_Temperature",
          neighbour_limit_type: "LL",
          step_size: 0.025,
          total_shift: 0.075,
        },
      ],
      columns: [
        { key: "entry_var", label: "Entry Variable" },
        { key: "entry_limit_type", label: "Entry Limit Type" },
        { key: "neighbour_var", label: "Neighbour Variable" },
        { key: "neighbour_limit_type", label: "Neighbour Limit Type" },
        { key: "step_size", label: "Step Size", type: "number" },
        { key: "total_shift", label: "Total Shift", type: "number" },
      ],
    };
  },
  methods: {
    handleAdd() {
      const newRow = {
        entry_var: "",
        entry_limit_type: "",
        neighbour_var: "",
        neighbour_limit_type: "",
        step_size: 0,
        total_shift: 0,
      };
      this.tableData.push(newRow);
    },
    handleDelete(rowIndex) {
      this.tableData.splice(rowIndex, 1);
    },
    handleSave(rowIndex) {
      console.log("Saved row:", this.tableData[rowIndex]);
    },
  },
};
</script>
