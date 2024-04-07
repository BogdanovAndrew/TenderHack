<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-blue-100">
    <div class="form-container">
      <input v-model="productName" class="input" type="text" placeholder="Название товара">
      <button @click="fetchProperties" class="btn">Запросить свойства</button>
    </div>
    <div v-if="properties.length > 0" class="properties-container">
      <div v-for="(type, property) in properties" :key="property" class="property-row">
        <label :for="property" class="property-label">{{ property }}:</label>
        <input :id="property" v-model="values[property]" type="text" class="input">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      productName: '',
      properties: {},
      values: {},
    };
  },
  methods: {
    async fetchProperties() {
      // Замените URL вашим эндпоинтом API
      const response = await fetch('URL_ВАШЕГО_API', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ productName: this.productName }),
      });
      if (response.ok) {
        const data = await response.json();
        this.properties = data;
        this.values = Object.keys(data).reduce((acc, key) => ({ ...acc, [key]: '' }), {});
      }
    },
  },
};
</script>

<style scoped>
.form-container, .properties-container {
  @apply w-full max-w-xs;
}

.property-row {
  @apply flex items-center mb-2;
}

.property-label {
  @apply mr-2;
}

.input {
  @apply block w-full px-4 py-2 mt-2 bg-white border rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50;
}

.btn {
  @apply mt-4 px-4 py-2 bg-blue-500 text-white font-semibold rounded-md shadow hover:bg-blue-600;
}
</style>
