new Vue({el:'#app',vuetify:new Vuetify(),data(){return{isDark:"white",}},methods:{ToggleTheme:function(){this.$vuetify.theme.dark=!this.$vuetify.theme.dark;if(this.isDark=="white"){this.isDark="black";}else{this.isDark="white";}},}});