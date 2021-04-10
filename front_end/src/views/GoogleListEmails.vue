<template>
  <h1>Google List Emails</h1>
</template>


<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "GoogleListEmails",
  async mounted() {
    let uri = "https://people.googleapis.com";
    uri += "/v1/people/me/connections?personFields=emailAddresses";
    uri += "&access_token=" + this.$route.params.token;
    uri += "&page_size=" + 100;
    const response = await fetch(uri);
    const json = await response.json();

    interface IConnections {
      [index: number]: {
        resourceName: string;
        etag: string;
        emailAddresses?: string;
      };
      [Symbol.iterator](): any;
    }
    const connections: IConnections = json.connections;
    for (let connection of connections) {
      if (!connection.emailAddresses) continue;
      console.log(connection.emailAddresses);
    }
  },
});
</script>

<style>
</style>