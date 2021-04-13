<template>
  <h1>Home page</h1>
  <button
    v-on:click="oauthLogin()"
    class="waves-effect waves-light btn-large red"
  >
    Login com Goole</button
  ><br /><br />
  <button
    v-on:click="customBackendLogin()"
    class="waves-effect waves-light btn-large blue"
  >
    Login com Back End customizado</button
  ><br />
</template>

<script lang="ts">
import { defineComponent } from "vue";

const URL = "https://accounts.google.com/o/oauth2/v2/auth";
const SCOPE = "https://www.googleapis.com/auth/contacts.readonly";

interface IObjectKeys {
  [key: string]: string;
}
interface IParametersInterface extends IObjectKeys {
  client_id: string;
  redirect_uri: string;
  response_type: string;
  scope: string;
}

const OAUTH_PARAMETERS: IParametersInterface = {
  client_id: process.env.VUE_APP_GOOGLE_OAUTH_CLIENT_ID,
  redirect_uri:
    process.env.VUE_APP_GOOGLE_OAUTH_REDIRECT_URL + "/google_redirect",
  response_type: "token",
  scope: SCOPE,
};

export default defineComponent({
  name: "Home",
  methods: {
    oauthLogin() {
      let uri = URL + "?";
      for (let parameter in OAUTH_PARAMETERS)
        uri += `&${parameter}=${OAUTH_PARAMETERS[parameter]}`;
      window.location.href = uri;
    },
    customBackendLogin() {
      this.$router.push({ name: "Custom Backend" });
    },
  },
});
</script>

<style scoped></style>
