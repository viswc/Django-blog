new Vue({el:'#app',vuetify:new Vuetify(),data(){return{BlogSlide:0;}},methods:{ToggleTheme:function(){this.$vuetify.theme.dark=!this.$vuetify.theme.dark;},}});