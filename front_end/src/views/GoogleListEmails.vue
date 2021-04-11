<template>
  <h1>Domínios e emails na sua conta Google</h1>
  <EmailTable :domains="domains" />
  <button v-on:click="back()" class="waves-effect waves-light btn-large red">
    Voltar</button
  ><br />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { IDomains, IJsonResponse, IConnections } from "../interfaces";
import EmailTable from "../components/EmailTable.vue";

export default defineComponent({
  name: "GoogleListEmails",
  data: () => {
    let data: { domains: IDomains } = {
      domains: {},
    };
    return data;
  },
  methods: {
    back() {
      this.$router.go(-2);
    },
  },
  components: {
    EmailTable,
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
</style>
