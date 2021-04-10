<template>
  <h1>Google List Emails</h1>
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

interface IConnections {
  [index: number]: {
    resourceName: string;
    etag: string;
    emailAddresses?: {
      [index: number]: {
        value: string;
      };
    };
  };
  [Symbol.iterator](): any;
}
interface IJsonResponse {
  nextPageToken: string | undefined;
  connections: IConnections;
}

export default defineComponent({
  name: "GoogleListEmails",
  data: () => {
    let data: {
      domains: { [key: string]: [string] | [] };
    } = {
      domains: {},
    };
    return data;
  },
  async mounted() {
    let uri = "https://people.googleapis.com";
    uri += "/v1/people/me/connections?personFields=emailAddresses";
    uri += "&access_token=" + this.$route.params.token;
    uri += "&page_size=" + 1000;

    let nextPageToken = null;
    do {
      let localUri = uri;
      if (nextPageToken) localUri += "&pageToken=" + nextPageToken;

      const response = await fetch(localUri);
      const json: IJsonResponse = await response.json();
      nextPageToken = json.nextPageToken;

      const connections: IConnections = json.connections;
      for (let connection of connections) {
        const emails = connection.emailAddresses;
        if (!emails) continue;
        for (let email of emails) {
          const emailAddress: string = email.value;
          const [user, domain] = emailAddress.split("@");
          if (!this.domains[domain]) this.domains[domain] = [];
          this.domains[domain].splice(this.domains[domain].length, 0, user);
        }
      }
    } while (nextPageToken);
  },
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