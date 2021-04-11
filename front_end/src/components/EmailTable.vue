<template>
  <table class="striped centered red lighten-4">
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
// import { IDomains } from "../interfaces";

export default defineComponent({
  name: "EmailTable",
  props: ["domains"],
});
</script>
