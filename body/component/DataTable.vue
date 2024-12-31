<template>
  <div class="data-table-container">
    <!-- Table Header -->
    <div class="table-header">
      <h3 class="table-title">{{ title }}</h3>
      <div class="action-buttons">
        <button @click="addRow" class="btn btn-success">
          <i class="fas fa-plus"></i> Add Row
        </button>
        <button @click="downloadData" class="btn btn-primary">
          <i class="fas fa-download"></i> Download Data
        </button>
      </div>
    </div>

    <!-- Table -->
    <div class="table-responsive">
      <table class="table">
        <thead>
          <tr>
            <th v-for="column in columns" :key="column.key">
              {{ column.label }}
            </th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <!-- Empty State -->
          <tr v-if="data.length === 0">
            <td :colspan="columns.length + 1" class="empty-state">
              No data available
            </td>
          </tr>

          <!-- Table Rows -->
          <tr
            v-for="(row, rowIndex) in data"
            :key="rowIndex"
            class="table-row"
          >
            <td v-for="column in columns" :key="column.key">
              <!-- Editable Cell -->
              <input
                v-if="editMode"
                v-model="row[column.key]"
                :type="column.type || 'text'"
                class="editable-input"
              />
              <span v-else>{{ row[column.key] }}</span>
            </td>
            <td>
              <!-- Action Buttons -->
              <div class="action-buttons">
                <button
                  @click="editRow(rowIndex)"
                  class="btn btn-warning btn-sm"
                  v-if="!editMode"
                >
                  <i class="fas fa-edit"></i> Edit
                </button>
                <button
                  @click="saveRow(rowIndex)"
                  class="btn btn-success btn-sm"
                  v-if="editMode"
                >
                  <i class="fas fa-save"></i> Save
                </button>
                <button
                  @click="deleteRow(rowIndex)"
                  class="btn btn-danger btn-sm"
                >
                  <i class="fas fa-trash"></i> Delete
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "DataTable",
  props: {
    title: {
      type: String,
      default: "Table Title",
    },
    data: {
      type: Array,
      required: true,
    },
    columns: {
      type: Array,
      required: true,
    },
  },
  emits: ["update:data", "add", "delete", "save"],
  data() {
    return {
      editMode: false, // Controls whether cells are editable
    };
  },
  methods: {
    editRow(rowIndex) {
      this.editMode = true;
      this.$emit("edit", rowIndex);
    },
    saveRow(rowIndex) {
      this.editMode = false;
      this.$emit("save", rowIndex);
    },
    deleteRow(rowIndex) {
      this.$emit("delete", rowIndex);
    },
    addRow() {
      this.$emit("add");
    },
    downloadData() {
      const blob = new Blob([JSON.stringify(this.data, null, 2)], {
        type: "application/json",
      });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.download = "table-data.json";
      link.click();
    },
  },
};
</script>

<style>
/* Container Styling */
.data-table-container {
  max-width: 100%;
  margin: auto;
  padding: 20px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* Header Styling */
.table-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.table-title {
  font-size: 1.5rem;
  color: #333;
}

.action-buttons button {
  margin-left: 10px;
}

/* Table Styling */
.table-responsive {
  overflow-x: auto;
}

.table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  margin-top: 10px;
}

.table th,
.table td {
  border: 1px solid #ddd;
  padding: 10px;
}

.table th {
  background-color: #f9fafb;
  color: #333;
  font-weight: bold;
}

.table-row:hover {
  background-color: #f1f5f9;
}

.empty-state {
  text-align: center;
  font-style: italic;
  color: #888;
}

/* Input Field Styling */
.editable-input {
  width: 100%;
  padding: 5px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

/* Button Styling */
.btn {
  border: none;
  padding: 5px 10px;
  border-radius: 4px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-sm {
  padding: 3px 8px;
}

.btn-primary {
  background-color: #007bff;
  color: white;
}

.btn-success {
  background-color: #28a745;
  color: white;
}

.btn-warning {
  background-color: #ffc107;
  color: black;
}

.btn-danger {
  background-color: #dc3545;
  color: white;
}

.btn:hover {
  opacity: 0.9;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .table-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .action-buttons button {
    margin-left: 0;
    margin-top: 5px;
  }
}
</style>
