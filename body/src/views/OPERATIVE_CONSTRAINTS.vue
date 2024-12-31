<template>
  <div>
    <h1>Operative Constraints Dashboard</h1>
    <DataTable
      :title="'Operative Constraints'"
      :data="tableData"
      :columns="columns"
      @add="handleAdd"
      @delete="handleDelete"
      @save="handleSave"
    />
  </div>
</template>

<script>
import axios from "axios";
import DataTable from "../../component/DataTable.vue";

export default {
  name: "OperativeConstraintsDashboard",
  components: { DataTable },
  data() {
    return {
      tableData: [],
      columns: [
        { key: "SrNo", label: "Sr No", type: "number", editable: false },
        { key: "Operative_Var", label: "Operative Var", editable: true },
        { key: "Read_SP", label: "Read SP", editable: true },
        { key: "Write_SP", label: "Write SP", editable: true },
        { key: "Opr_LL", label: "Opr LL", type: "number", editable: true },
        { key: "Opr_UL", label: "Opr UL", type: "number", editable: true },
        { key: "Min_Step", label: "Min Step", type: "number", editable: true },
        { key: "Max_Step", label: "Max Step", type: "number", editable: true },
        { key: "Selection", label: "Selection", editable: true },
        { key: "Cost", label: "Cost", type: "number", editable: true },
        { key: "Median_Val", label: "Median Value", type: "number", editable: true },
        { key: "constraint_30min", label: "Constraint 30min", type: "number", editable: true },
      ],
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/operative-constraints");
        this.tableData = response.data;
      } catch (error) {
        console.error("Error fetching data:", error);
        alert("Failed to fetch data from the server.");
      }
    },
    async handleAdd() {
      const newRow = {
        Operative_Var: "",
        Read_SP: "",
        Write_SP: "",
        Opr_LL: 0,
        Opr_UL: 0,
        Min_Step: 0,
        Max_Step: 0,
        Selection: "",
        Cost: 0,
        Median_Val: 0,
        constraint_30min: 0,
      };
      try {
        const response = await axios.post("http://127.0.0.1:8000/operative-constraints", newRow);
        this.tableData.push(response.data);
        alert("New row added successfully.");
      } catch (error) {
        console.error("Error adding row:", error);
        alert("Failed to add new row.");
      }
    },
    async handleDelete(rowIndex) {
      const srno = this.tableData[rowIndex].SrNo;
      try {
        await axios.delete(`http://127.0.0.1:8000/operative-constraints/${srno}`);
        this.tableData.splice(rowIndex, 1);
        alert("Row deleted successfully.");
      } catch (error) {
        console.error("Error deleting row:", error);
        alert("Failed to delete row.");
      }
    },
    async handleSave(rowIndex) {
      const updatedRow = this.tableData[rowIndex];
      const srno = updatedRow.SrNo;
      try {
        await axios.put(`http://127.0.0.1:8000/operative-constraints/${srno}`, updatedRow);
        alert("Row updated successfully.");
      } catch (error) {
        console.error("Error updating row:", error);
        alert("Failed to update row.");
      }
    },
  },
};
</script>

<style>
h1 {
  text-align: center;
  margin: 20px 0;
}
</style>
