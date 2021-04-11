<template>
  <table>
    <tr>
      <th>Domínio</th>
      <th>Emails</th>
    </tr>
    <tr v-for="(domainItems, domainName) in domains" :key="domainName">
      <td>{{ domainName }}</td>
      <td>
        <span v-for="item in domainItems" :key="item">
          {{ item }}@{{ domainName }}<br />
        </span>
      </td>
    </tr>
  </table>
</template>

<script lang="ts">
import { defineComponent } from "vue";
// import { IDomains } from "../interfaces";

export default defineComponent({
  name: "EmailTable",
  props: ["domains"],
});
</script>

<style scoped>
table,
th,
td,
tr {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>