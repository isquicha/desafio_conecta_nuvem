<template>
  <h1>Custom Backend</h1>
  <div v-if="status === 'login'">
    <form class="form">
      <input
        type="text"
        placeholder="username"
        v-model="username"
        autocomplete="username"
      />
      <input
        type="password"
        placeholder="password"
        v-model="password"
        autocomplete="current-password"
      />
    </form>
    <button
      v-on:click="login()"
      class="waves-effect waves-light btn-large blue"
    >
      Login</button
    ><br />
  </div>
  <div v-if="status === 'logged'">
    <EmailTable :domains="domains" color="blue" /><br />
    <button v-on:click="back()" class="waves-effect waves-light btn-large blue">
      Voltar</button
    ><br />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { IDomains } from "../interfaces";
import EmailTable from "../components/EmailTable.vue";

const BACKEND_URL = process.env.VUE_APP_CUSTOM_BACKEND_URL + "/api/v1";
const TOKEN_URL = BACKEND_URL + "/user/token/";
const CONTACTS_URL = BACKEND_URL + "/contacts/";

export default defineComponent({
  name: "Custom Backend",
  components: {
    EmailTable,
  },
  data: () => {
    let data: { domains: IDomains; [key: string]: any } = {
      status: "login",
      username: "",
      password: "",
      access_token: "",
      domains: {},
    };
    return data;
  },
  methods: {
    async login() {
      const response = await fetch(TOKEN_URL, {
        headers: { "Content-Type": "application/json" },
        method: "POST",
        body: JSON.stringify({
          username: this.username,
          password: this.password,
        }),
      });
      const json = await response.json();
      try {
        if (json.payload.access_token) {
          this.status = "logged";
          this.access_token = json.payload.access_token;
          await this.getContacts();
        }
      } catch (e) {
        return;
      }
    },
    async getContacts() {
      const response = await fetch(
        CONTACTS_URL + `?access_token=${this.access_token}`
      );
      const json = await response.json();
      const contacts = json.payload.contacts;
      for (let contact in contacts) {
        for (let email of contacts[contact]) {
          const [user, domain] = email.split("@");
          if (!this.domains[domain]) this.domains[domain] = [];
          this.domains[domain].splice(this.domains[domain].length, 0, user);
        }
      }
    },
    back() {
      this.$router.go(-1);
    },
  },
});
</script>
