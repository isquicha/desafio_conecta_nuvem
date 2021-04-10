<template>
  <h1>Google List Emails</h1>
  <ul>
    <li v-for="email in emailList" :key="email">
      {{ email }}
    </li>
  </ul>
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

export default defineComponent({
  name: "GoogleListEmails",
  data: () => {
    let data: { emailList: [string] | [] } = {
      emailList: [],
    };
    return data;
  },
  computed: {},

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
      const json = await response.json();
      nextPageToken = json.nextPageToken;
      const connections: IConnections = json.connections;

      for (let connection of connections) {
        const emails = connection.emailAddresses;
        if (!emails) continue;
        for (let email of emails) {
          // ? Insert the email at the end of the emailList
          this.emailList.splice(this.emailList.length, 0, email.value);
        }
      }
    } while (nextPageToken);
  },
});
</script>

<style>
</style>