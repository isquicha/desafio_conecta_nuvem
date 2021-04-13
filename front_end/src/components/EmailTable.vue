<template>
  <table class="striped centered lighten-4" :class="color">
    <thead>
      <tr>
        <th>Domínio</th>
        <th>Emails</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(domainItems, domainName) in domains" :key="domainName">
        <td>{{ domainName }}</td>
        <td>
          <span v-for="item in domainItems" :key="item">
            {{ item }}@{{ domainName }}<br />
          </span>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "EmailTable",
  props: {
    domains: {},
    color: {
      default: "red",
    },
  },
});
</script>
