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
import axios from 'axios';
import DataTable from "../../component/DataTable.vue";

export default {
  name: "OperationalConstraintsDashboard",
  components: { DataTable },
  data() {
    return {
      tableData: [], // Stores data fetched from the backend
      columns: [
        { key: "Station", label: "Station" }, // Updated column names
        { key: "OPC_Tag", label: "OPC Tag" },
        { key: "Readable_Tag", label: "Readable Tag" },
        { key: "Description", label: "Description" },
        { key: "Data_Type", label: "Data Type" },
        
        
        { key: "id", label: "ID", type: "number" }, // 'id' as part of columns for editing
      ],
    };
  },
  methods: {
    // Fetch data from the backend
    async fetchData() {
      try {
        const response = await axios.get('http://localhost:8000/operational_tag');
        this.tableData = response.data;
      } catch (error) {
        console.error("There was an error fetching data:", error);
      }
    },
    // Handle addition of a new row
    async handleAdd() {
      const newRow = {
        Station: "",
        OPC_Tag: "",
        Readable_Tag: "",
        Description: "",
        Data_Type: "N", // Default value
        
        // Do not include the 'id' for a new entry
      };
      try {
        const response = await axios.post('http://localhost:8000/operational_tag', newRow);
        this.tableData.push(response.data); // Backend will return the entry with an auto-generated 'id'
      } catch (error) {
        console.error("Error adding row:", error);
      }
    },
    // Handle deletion of a row
    async handleDelete(rowIndex) {
      const rowToDelete = this.tableData[rowIndex];
      try {
        await axios.delete(`http://localhost:8000/operational_tag/${rowToDelete.id}`);
        this.tableData.splice(rowIndex, 1);
      } catch (error) {
        console.error("Error deleting row:", error);
      }
    },
    // Handle saving an updated row
    async handleSave(rowIndex) {
      const rowToUpdate = this.tableData[rowIndex];
      const updatedRow = {
        id: rowToUpdate.id, // Include the 'id' from the available data
        Station: rowToUpdate.Station,
        OPC_Tag: rowToUpdate.OPC_Tag,
        Readable_Tag: rowToUpdate.Readable_Tag,
        Description: rowToUpdate.Description,
        Data_Type: rowToUpdate.Data_Type,
        
      };
      try {
        const response = await axios.put(`http://localhost:8000/operational_tag/${rowToUpdate.id}`, updatedRow);
        this.tableData.splice(rowIndex, 1, response.data); // Replace the updated row
      } catch (error) {
        console.error("Error saving row:", error);
      }
    },
  },
  mounted() {
    this.fetchData(); // Fetch data when the component is mounted
  },
};
</script>
