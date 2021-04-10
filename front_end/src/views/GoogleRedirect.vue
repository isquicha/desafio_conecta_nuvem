<template>
  <h1>Google Redirect</h1>
</template>


<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "GoogleRedirect",
  mounted() {
    const hash = this.$route.hash.toString().substring(1);
    const parameters = hash.split("&");
    let token = null;
    let error = null;

    for (let parameter of parameters) {
      const [name, value] = parameter.split("=");
      if (name == "access_token") {
        token = value;
        break;
      }
      if (name == "error") {
        error = value;
        break;
      }
    }
    if (token)
      this.$router.push({
        name: "Google List Emails",
        params: { token: token },
      });
    if (error) console.log(error);
  },
});
</script>

<style>
</style>