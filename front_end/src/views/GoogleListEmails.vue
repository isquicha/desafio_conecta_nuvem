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
import { IDomains, IJsonResponse, IConnections } from "../interfaces";

export default defineComponent({
  name: "GoogleListEmails",
  data: () => {
    let data: { domains: IDomains } = {
      domains: {},
    };
    return data;
  },
  created() {
    getEmails(this.$route.params.token, this.domains);
  },
});

const getEmails = async (token: string | string[], domainsList: IDomains) => {
  let uri = "https://people.googleapis.com";
  uri += "/v1/people/me/connections?personFields=emailAddresses";
  uri += "&access_token=" + token;
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
        if (!domainsList[domain]) domainsList[domain] = [];
        domainsList[domain].splice(domainsList[domain].length, 0, user);
      }
    }
  } while (nextPageToken);
};
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
