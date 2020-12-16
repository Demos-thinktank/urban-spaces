import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/most-urgent",
    name: "MostUrgent",
    // route level code-splitting
    // this generates a separate chunk (most-urgent.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "MostUrgent" */ "../views/MostUrgent.vue")
  },
  {
    path: "/covid-effect",
    name: "CovidEffect",
    component: () => import("../views/CovidEffect.vue")
  },
  {
    path: "/satisfaction-index",
    name: "SatisfactionIndex",
    component: () => import("../views/SatisfactionIndex.vue")
  },
  {
    path: "/read-the-report",
    name: "ReadTheReport",
    component: () => import("../views/ReadTheReport.vue")
  },
  { path: "*", redirect: "/" }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
