import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Home from "../views/Home.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/google_redirect",
    name: "Google Redirect",
    component: () => import("../views/GoogleRedirect.vue"),
  },
  {
    path: "/google_list_emails",
    name: "Google List Emails",
    component: () => import("../views/GoogleListEmails.vue"),
  },

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
